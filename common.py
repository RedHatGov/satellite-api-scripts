#!/usr/bin/python

# CHANGELOG:
# * Fri Nov 29 2013 Shawn Wells <shawn@redhat.com> 1.0
#       - Initial version of login() and logout()

import sys, xmlrpclib

# RHN_URL https://hostname/rpc/api <-- remember the /rpc/api!
RHN_URL = "https://satellite.phx.salab.redhat.com/rpc/api"
RHN_USERNAME = "put_your_username_here"
RHN_PASSWORD = "put_your_password_here"

def login():
        client = xmlrpclib.Server(RHN_URL, verbose=0)
        sessionkey = client.auth.login(RHN_USERNAME, RHN_PASSWORD)
        return client, sessionkey


def logout(client, sessionkey):
        client.auth.logout(sessionkey)
