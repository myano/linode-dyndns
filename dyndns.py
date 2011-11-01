#!/usr/bin/env python
"""
dyndns.py -- Dynamic DNS for Linode
Copyright 2011 Michael S. Yanovich

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


This script is a dynamic dns script for Linode. Simply provide the
appropriate command line arguments and it will update the IP address in
Linode's Domain Manager.
"""

import argparse
import api
import sys
import urllib2

def getip():
    u = urllib2.urlopen("http://yano.me/ip/")
    ip = u.read().rstrip().lstrip()
    u.close()
    return ip

def updateip(apikey, domain_name, subdomain, port, domain_type):
    if port == None:
        port = 22
    if domain_type == None:
        domain_type = "A"

    FLAG = True
    linode = api.Api(apikey)
    domains = linode.domain_list()

    for domain in domains:
        if domain["DOMAIN"] == domain_name:
            did = domain["DOMAINID"]

    for each in linode.domain_resource_list(DomainID=did):
        if each["NAME"] == subdomain:
            FLAG = False

    ## grab IP address
    ip = getip()
    if FLAG == True:
        a = linode.domain_resource_create(Port=port, DomainID=did,
                Type=domain_type, Name=subdomain, Target=ip)
        print a

def main():
    desc = "This script is a Dynamic DNS updater for Linode."

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-p', type=int, dest='port',
            help='specifies the port number')
    parser.add_argument('-ak', action='store', dest='apikey',
            required=True, help='specifies the api key')
    parser.add_argument('-dt', action='store', dest='domain_type',
            help='specifies the domain type')
    parser.add_argument('-dn', action='store', dest='domain_name',
            required=True, help='specifies the domain name')
    parser.add_argument('-sd', action='store', dest='subdomain',
            required=True, help='specifies the subdomain')
    results = parser.parse_args()

    updateip(results.apikey, results.domain_name, results.subdomain,
            results.port, results.domain_type)

if __name__ == '__main__':
    main()
