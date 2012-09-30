#!/usr/bin/env python

"""   
   Send SMS message via Nexmo
  ------------------------------
   Brian Parsons <brian@pmex.com>


Requires: libpynexmo https://github.com/marcuz/libpynexmo

"""

##
## CONFIGURATION VARIABLES
##

nexmoreqtype = "json"
nexmouser = ""
nexmopass = ""
nexmosendnumber = ""

# Libraries

import sys
from nexmomessage import NexmoMessage

# Process command line, show usage information if not valid number of arguments

if len(sys.argv) < 3:
        print "Usage: %s <number> <message>" % sys.argv[0]
        sys.exit(1)
else:
        sendto = sys.argv[1]
        restofline = sys.argv[2:]

message = ''

if type(restofline) in [list, tuple, set]:
        for argument in restofline:
                message += ' ' + argument

message = message.strip()

print "Sending \'%s\' to %s..." % (message, sendto)

nexmomsg = {'reqtype': nexmoreqtype, 'password': nexmopass, 'from': nexmosendnumber, 'to': sendto, 'username': nexmouser, 'text': message }
sms1 = NexmoMessage(nexmomsg)
sms1.set_text_info(message)
print sms1.send_request()

