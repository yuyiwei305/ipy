#! /usr/bin/env python

from IPy import IP

ip_s = raw_input(" pls input your ip :  ")

ips = IP(ip_s)

if len(ips) > 1 :
	print "net : %s " % ips.net()
	print "netmask : %s " %  ips.netmask()
	print "broadcast : %s "  % ips.broadcast()
	print "reverse address : %s " %  ips.reverseNames()[0]
	print "subnet : %s " % len(ips)
else : 
	print "reverse address : %s " %  ips.reverseNames()[0]
print "hexadecimal : %s " % ips.strHex()
print "binary ip : %s " % ips.strBin()
print "iptype : %s" % ips.iptype()
