#!/usr/bin/python
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

#for proxy authenticated internet: code_starts
proxy = urllib2.ProxyHandler({'http':'http://d.khatri:take2tulsi@localhost:8323'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy,auth,urllib2.HTTPBasicAuthHandler)
urllib2.install_opener(opener)
#code_ends

#declare list here
url_list = ['www.google.com','www.iitg.ac.in','www.facebook.com','www.flipkart.com','www.goal.com']
#ping_stats.txt file to store the pinging stats
fo = open("ping_stats.txt", "w")
i = 0
while i<5:
	print i
	cnt = 0
	fo.write("PING stats for " + url_list[i])
	while cnt<20:
		url = "http://www.spfld.com/cgi-bin/ping?remote_host=" + url_list[i] + "&dns=on&count=10&size=64"
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		fo.write(soup.get_text())
		cnt = cnt + 1
	fo.write('\n')
	i = i + 1
i =6
fo.write("--------------------------------------------------------------------------------------------\n")
fo.write("Now Varying Package Sizes:\n")
#ping stats for different packet sizes: 64 bytes to 2048 bytes
while i<12:
	cnt=1
	size = 2**int(i)
	print size
	fo.write("Package: "+str(size)+" bytes")
	while cnt<21:
		fo.write("\nPING No.: "+str(cnt))
		url = "http://www.spfld.com/cgi-bin/ping?remote_host=" + str(url_list[0]) + "&dns=on&count=10&size="+str(size)
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		fo.write(soup.get_text())
		cnt = cnt + 1
	i = i + 1
