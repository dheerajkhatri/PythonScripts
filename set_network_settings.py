#
import os
print "Press l for localhost:8323 ---- Press m for Manual 202.141.80.19:3128"
input = raw_input()

Proxy = ""
Port = 0
is_right = 0

while is_right == 0:
	
	if input == "l":
		Proxy = "localhost"
		Port = 8323
		is_right = 1		
	
	elif input == "m":
		Proxy = "202.141.80.19"
		Port = 3128
		is_right = 1
	
	else :
		print "Wrong entries try again"
		input = raw_input()
		is_right = 0

os.system("gsettings set org.gnome.system.proxy.http host %s" %Proxy)
os.system("gsettings set org.gnome.system.proxy.https host %s" %Proxy)
os.system("gsettings set org.gnome.system.proxy.ftp host %s" %Proxy)
os.system("gsettings set org.gnome.system.proxy.socks host %s" %Proxy)

os.system("gsettings set org.gnome.system.proxy.http port %d" %Port)
os.system("gsettings set org.gnome.system.proxy.https port %d" %Port)
os.system("gsettings set org.gnome.system.proxy.ftp port %d" %Port)
os.system("gsettings set org.gnome.system.proxy.socks port %d" %Port)
print "--------------Changed Succefully-----------------"