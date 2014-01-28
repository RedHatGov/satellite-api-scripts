#!/usr/bin/env python
"""
Example script that uses the Satellite XMLRPC API to fetch the list of software
channels from RHN.

To run:
$ python ose_errata.py RHNusername RHNpassword
"""

import xmlrpclib
import sys

__author__ = 'Jason Callaway'
__email__ = 'jcallaway@redhat.com'
__license__ = 'GPL'
__version__ = '0.1'


USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

SATELLITE_FQDN = 'rhn.redhat.com'
SATELLITE_URL = 'https://' + SATELLITE_FQDN + '/rpc/api'

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(USERNAME, PASSWORD)

channels = client.channel.listSoftwareChannels(key)
channel_list = []
for c in channels:
	if 'ose' in c['channel_label'] and not 'beta' in c['channel_label'] and not 'debug' in c['channel_label']:
		channel_list.append(c['channel_label'])
	if 'osop' in c['channel_label'] and not 'beta' in c['channel_label'] and not 'debug' in c['channel_label']:
		channel_list.append(c['channel_label'])

advisory_count = 0
rhsa_count = 0
cve_count = 0
output_list = []
for channel in channel_list:
	for e in client.channel.software.listErrata(key, channel, '1970-01-01'):
		advisory_count = advisory_count + 1
		if 'RHSA' in e['errata_advisory']:
			rhsa_count = rhsa_count + 1
		cve_list = client.errata.listCves(key, e['errata_advisory'])
		cve_count = cve_count + len(cve_list)
		output_list.append('"' + channel + '","' + e['errata_advisory'] + '","' + e['errata_issue_date'] + '","' + e['errata_synopsis'] + '","' + '","'.join(cve_list) + '"')
print '"total advisories","' + str(advisory_count) + '"'
print '"security advisories","' + str(rhsa_count) + '"'
print '"CVEs addressed","' + str(cve_count) + '"'
print '\n'.join(output_list)
