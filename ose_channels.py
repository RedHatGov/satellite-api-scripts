#!/usr/bin/env python
"""
Example script that uses the Satellite XMLRPC API to fetch the list of software
channels from RHN.

To run:
$ python ose_python.py RHNusername RHNpassword
"""

import xmlrpclib
import sys
import pprint

__author__ = 'Jason Callaway'
__email__ = 'jcallaway@redhat.com'
__license__ = 'GPL'
__version__ = '0.1'

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

pp = pprint.PrettyPrinter(indent=4)

SATELLITE_FQDN = 'rhn.redhat.com'
SATELLITE_URL = 'https://' + SATELLITE_FQDN + '/rpc/api'

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(USERNAME, PASSWORD)

channels = client.channel.listSoftwareChannels(key)
pp.pprint(channels)
