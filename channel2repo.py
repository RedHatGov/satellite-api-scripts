#!/usr/bin/python

# CHANGELOG:
# Based on channel2repo.py by Rhys Oxenham <roxenham@redhat.com>
# * Fri Nov 29 2013 Shawn Wells <shawn@redhat.com> 1.0
#       - Initial version
#	- Updated to use login from common.py

# USAGE:
# example usage (e.g. for RHEV 3.1 beta + CloudForms v1 w/deps)
# ./channel2repo.py --createrepo -c jbappplatform-6-x86_64-server-6-rpm -c rhel-x86_64-rhev-agent-6-server-beta -c rhel-x86_64-rhev-mgmt-agent-6-beta -c rhel-x86_64-server-6 -c rhel-x86_64-server-6-cf-ce-1 -c rhel-x86_64-server-6-cf-se-1 -c rhel-x86_64-server-6-cf-tools-1 -c rhel-x86_64-server-6-rhevm-3-beta -c rhel-x86_64-server-optional-6 -c rhel-x86_64-server-supplementary-6 -c rhn-tools-rhel-x86_64-server-6
#
# Note: If you recieve argparse errors, 'yum install python-argparse'

import argparse
import os
import sys
import urllib
import xmlrpclib
import common

def parse_args():
  ap = argparse.ArgumentParser()
  ap.add_argument("-c", "--channel", default = [], dest = "channels",
                  nargs = "+")
  ap.add_argument("--createrepo", action = "store_true")
  return ap.parse_args()

if __name__ == "__main__":
  args = parse_args()

  (client, sessionKey) = common.login()

  for channel in args.channels:
    print >>sys.stderr, "Dumping channel %s..." % channel
    if not os.path.exists(channel):
      os.mkdir(channel)

    pkgs = client.channel.software.listLatestPackages(sessionKey, channel)
    for i, pkg in enumerate(pkgs):
      filename = client.packages.getDetails(sessionKey, pkg["id"])["file"]
      print >>sys.stderr, "[%u/%u] %s" % (i + 1, len(pkgs), filename)
      urllib.urlretrieve(client.packages.getPackageUrl(sessionKey, pkg["id"]),
                         os.path.join(channel, filename))

  client.auth.logout(sessionKey)

  if args.createrepo:
    os.system("createrepo .")
