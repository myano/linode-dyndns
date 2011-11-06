=============
Linode-DYNDNS
=============

This script, dyndns.py, is a python script that automatically updates a
subdomain in your Domain Manager on your Linode account with the current IP
address. This script was designed to be executed from a cronjob. It can also
be executed on it's own and it will update the appropriate settings.

Package requires:

python-pycurl
python >= 2.6


Run
---

``./dyndns.py -ak your_api_key -dn example.org -sd foo``

This will create a subdomain 'foo.example.org' that points to your existing
IP address on the machine that it is executed from.


Trouble / Help
--------------

1.) If you get the error message, ``using urllib instead of pycurl, urllib does 
not verify SSL remote certificates, there is a risk of compromised 
communication``

You'll need to install pycurl.

2.) If you get the error message, ``api.ApiError: [{u'ERRORCODE': 4, 
u'ERRORMESSAGE': u'Authentication failed'}]``

Double check your API key, as Linode was unable to authenticate your key.


License
-------

This script is license under the GNU GPL v3.
