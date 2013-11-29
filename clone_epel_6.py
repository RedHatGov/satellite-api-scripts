#!/usr/bin/python

# CHANGELOG:
# * Fri Nov 29 2013 Shawn Wells <shawn@redhat.com> 1.0
#	- Initial version

# ABOUT:
# This script will clone the EPEL6 repository into a child of
# rhel-x86_64-server-6.

# Manual steps are documented @
# https://access.redhat.com/site/solutions/308983

import xmlrpclib
import common

print 'Step 0: Login . . .',
(client, sessionKey) = common.login()
print '[OK]'

print 'Step 1: Create rhel-x86_64-server-6-epel as child of rhel-x86_64-server-6 . . .',
client.channel.software.create(sessionKey,
				'rhel-x86_64-server-6-epel',
				'EPEL 6 x86_64',
				'Extra Packages for Enterprise Linux 6 x86_64',
				'channel-x86_64',
				'rhel-x86_64-server-6',
				'sha256')
print '[OK]'

print 'Step 2: Create repo repo-rhel-x86_64-server-6-epel . . .',
client.channel.software.createRepo(sessionKey,
				'repo-rhel-x86_64-server-6-epel',
				'yum',
				'http://mirrors.servercentral.net/fedora/epel/6/x86_64/')
print '[OK]'

print 'Step 3: Associate EPEL repo to EPEL channel . . .',
client.channel.software.associateRepo(sessionKey,
					'rhel-x86_64-server-6-epel',
					'repo-rhel-x86_64-server-6-epel')
print '[OK]'

print 'Step 4: Initiating repo sync . . .',
client.channel.software.syncRepo(sessionKey, 'rhel-x86_64-server-6-epel')
print '[OK]'

print 'Step 5: Logout . . .',
common.logout(client, sessionKey)
print '[OK]'
print 'At this point, EPEL 6 will be syncing to your satellite. This may take some time. Grab a coffee.'
