#coding:utf-8

# Labb 3 Uppgift 3a - ggn14002

import subprocess
import netsnmp
import ipaddr
import sys

#First, check to see if we have 3 arguments (2 without arg0)
if ( len(sys.argv) == 3 ):
    #Test the first argument and see if it is an IP address. If it is, print error.
    try:
        com = ipaddr.IPv4Address(sys.argv[1])
        print "1Usage: %s [Community] [IP-Address]" % sys.argv[0]
    #If the try fails (so the community is NOT an IP address), continue on with next check
    except:
        #Test the second argument and see if it is an IP address. If it is, continue to the code. else print error.
        try:
            #Here comes the code after the tests have completed
            #First off, we want to do a snmpwalk with 'subprocess'  
            ipAddr = ipaddr.IPv4Address(sys.argv[2])
            ipAddr = sys.argv[2]
            com = sys.argv[1]
            a = subprocess.Popen(["snmpwalk","-v2c","-c",com,ipAddr,"ifDescr"],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
            print "snmpwalk of ifDescr with the module 'subprocess':"
            print a
            #Secondly, we do another snmpwalk but this time we use 'netsnmp'
            oid=netsnmp.Varbind("ifDescr")
            b = netsnmp.snmpwalk(oid,Version=2,DestHost=ipAddr,Community=com)
            print "snmpwalk of ifDescr with the module 'netsnmp':"
            print b
        except ipaddr.AddressValueError as e:
            print "2Usage: %s [Community] [IP-Address]" % sys.argv[0]          
else:
    print "3Usage: %s [Community] [IP-Address]" % sys.argv[0]
