import sys
import os
import datetime

from cryptography import x509
from cryptography.hazmat.backends import default_backend

from cfengine import PromiseModule, ValidationError

def validate_certificate(certificate_file, days=30):

    with open(certificate_file, 'rb') as fi:
        data = fi.read()

    try:
        days = int(days)
    except ValueError:
        days = 30

    cert = x509.load_pem_x509_certificate(data, default_backend())
    diff = cert.not_valid_after - datetime.datetime.now()

    if diff.days <= days:
        promise_failed = True
    else:
        promise_failed = False

    return promise_failed, "Certificate \'%s\' will expire within %s days" % (certificate_file, diff.days)

class CertificatePromiseTypeModule(PromiseModule):

    def validate_promise(self, promiser, attributes):
        pass

    def evaluate_promise(self, promiser, attributes):

        if not os.path.exists(promiser):
            self.log_error('Given path does not exists %s' % promiser)
            self.promise_not_kept()
        elif not os.path.isfile(promiser):
            self.log_error('Given path must be a file %s' % promiser)
            self.promise_not_kept()
        else:
            result, message = validate_certificate(promiser, **attributes)


            if result:
                self.log_error(message)
                self.promise_not_kept()
            else:
                self.log_info(message)
                self.promise_kept()


if __name__ == "__main__":
    CertificatePromiseTypeModule().start()
