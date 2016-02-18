#coding:utf-8

# Labb 3 Uppgift 4a - ggn14002

import sys
import subprocess
import netsnmp
import ipaddr

community = sys.argv[1]
ipAddr = sys.argv[2]

if (len(sys.argv) == 3):
	try:
		#If the first argument is an IP address, print a failure & exit.
		ipaddr.IPv4Address(community)
		print "Err: Invalid Community - Usage: %s [Community] [IP-Address]" % sys.argv[0]
		sys.exit(1)
	except:
		try:
			#Create a file for the current search
			file = open(ipAddr, 'w+')
			i=0
			#Use the variable 'oid' to bind netsnmp, then do a snmpwalk of that OID and save it to a variable for later.
			#Check the Interface Addresses
			oid = netsnmp.Varbind("ipAdEntAddr")
			ifAddr = netsnmp.snmpwalk(oid, Version = 2, DestHost = ipAddr, Community = community)
			#Check the Interface Ports
			oid = netsnmp.Varbind("ipAdEntIfIndex")
			ifPorts = netsnmp.snmpwalk(oid, Version = 2, DestHost = ipAddr, Community = community)
			#Check the Interface Netmasks
			oid = netsnmp.Varbind("ipAdEntNetMask")
			ifNetmask = netsnmp.snmpwalk(oid, Version = 2, DestHost = ipAddr, Community = community)
			#Check the System's Description
			oid = netsnmp.Varbind("sysDescr")
			description, = netsnmp.snmpwalk(oid, Version = 2, DestHost = ipAddr, Community = community)
			#Check the System Name
			oid = netsnmp.Varbind("sysName")
			sysName, = netsnmp.snmpwalk(oid, Version = 2, DestHost = ipAddr, Community = community)

			#Check if it is the Access Point. This uses a different OID, and if it isn't the AP, run the other OID
			if ipAddr == "192.168.152.14":
				oid = netsnmp.Varbind('.1.3.6.1.2.1.47.1.1.1.1.2.1')
				Model, = netsnmp.snmpget(oid, Version = 2, DestHost = ipAddr, Community = community)
			else:
				oid = netsnmp.Varbind('.1.3.6.1.2.1.47.1.1.1.1.13.1')
				Model, = netsnmp.snmpget(oid, Version = 2, DestHost = ipAddr, Community = community)
			
			#Start printing the information to the user
			print "\nHost: "+ipAddr
			file.write("Host: "+ipAddr)
			if Model is not None:
				print "Model: "+Model
				file.write("\nModel: "+Model)
			print "Name: "+sysName
			file.write("\nName: "+sysName)
			print "\nDescription: "+description
			file.write("\nDescription: "+description)
			print "\nInterface:		IP-Address		Netmask		MAC-Address"
			file.write("\nInterface:		IP-Address		Netmask		MAC-Address")
			print "\n--------------------------------------------------------------------------"
			file.write("\n--------------------------------------------------------------------------")
			#Goes through every interface currently being used & prints the formatted information of each
			for entries in ifPorts:
				temp1, = netsnmp.snmpget("ifDescr."+entries, Version = 2, DestHost = ipAddr, Community = community)
				temp2, = netsnmp.snmpget("ifPhysAddress."+entries, Version = 2, DestHost = ipAddr, Community = community)
				#Format the mac address
				mac = str(temp2)
				mac = mac.encode('hex')
				#Set the 'port' variable as the string of 'temp1'
				port = str(temp1)
				#Format the final print for the value currently being processed
				print '{:<20} {:<20} {:<20} {:<20}'.format(port, ifAddr[i], ifNetmask[i], mac)
				file.write('\n{:<20} {:<20} {:<20} {:<20}'.format(port, ifAddr[i], ifNetmask[i], mac))
				i=i+1
			file.close()
		except ipaddr.AddressValueError as e:
			print "Err: Address Value Error - Usage: %s [Community] [IP-Address]" % sys.argv[0]
			sys.exit(1)
else:
	print "Err: Too many arguments - Usage: %s [Community] [IP-Address]" % sys.argv[0]
	sys.exit(1)
