#!/usr/bin/env python
"""
Example script that uses the Satellite XMLRPC API to fetch the list of software
channels from RHN.

To run:
$ python rpm_changelog.py RHNusername RHNpassword channelName rpmName
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
CHANNEL = sys.argv[3]
RPM_NAME = sys.argv[4]

pp = pprint.PrettyPrinter(indent=4)

SATELLITE_FQDN = 'rhn.redhat.com'
SATELLITE_URL = 'https://' + SATELLITE_FQDN + '/rpc/api'

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(USERNAME, PASSWORD)

print 'Generating package list...'
channel_packages = client.channel.software.listAllPackages(key, CHANNEL)
for pkg in channel_packages:
	if pkg['package_name'] == RPM_NAME:
		print 'name: ' + pkg['package_name']
		print 'id: ' + str(pkg['package_id'])
		print 'changelog:'
		changelog = client.packages.listChangelog(key, pkg['package_id'])
		pp.pprint(changelog)
