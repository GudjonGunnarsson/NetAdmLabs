#!/usr/bin/python
# -*- coding: utf-8 -*-

# Labb 3 Uppgift 2c - ggn14002
#
# Accepterar en fil i argument eller låter användare
# skriva in en filsökväg och sorterar ut IP-adresser från denna.

import sys
import re

try: 
    if ( len(sys.argv[1:]) > 1 ):
        print "Too many arguments! Only one accepted!"
    elif sys.argv[1:]:
        print "File: %s" % (sys.argv[1])
        file = sys.argv[1]
    else:
        file = raw_input("Please enter a log file to parse: ")
    try:
        fileop = open(file, "r")
        ips = []
        for text in fileop.readlines():
            text = text.rstrip()
            findout = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', text)
            if findout is not None:
                for match in findout:
                    if match not in ips:
                        ips.append(match)
        for ip in ips:
            check = "".join(ip)
            if check is not '':
                if "255." not in check:
                    print "IP: %s" %check
    finally:
        fileop.close()
except IOError, (errno, strerror):
    print "I/O Error(%s) : %s" % (errno, strerror)
