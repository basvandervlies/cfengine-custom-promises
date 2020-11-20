# cfengine-custom-promises

Contains some test with the new CFengine 3.17 custom promise type. Uses the module from the
cfengine-core github repo located at:
 - https://github.com/cfengine/core/tree/master/docs/custom_promise_types

## certificate.py
A simple promise type to check when your certificate will expire, when within the "days" threshold the promise os not kepted and someone needs to doe something?

```
dennis@debian:~/cfengine-custom-promises$ cf-agent -f ./promise_test.cf
   error: Certificate '/etc/certificate/certificate.pem' will expire within 595 days
   error: Certificate '/etc/certificate/certificate.pem' will expire within 595 days
   error: Certificate '/etc/certificate/certificate.pem' will expire within 595 days
```
