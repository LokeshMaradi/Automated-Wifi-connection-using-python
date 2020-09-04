import os,sys
saved=os.popen("netsh wlan show profiles").read()
print(saved)
available=os.popen("netsh wlan show networks").read()
print(available)
ssid=input("Enter the connection which you want to establish:")
dis=os.popen("netsh wlan disconnect").read()
print(dis)
if ssid in available:
	print("Network exists")
else:
	print("Network does not exist")
	sys.exit()
while(1):
	available=os.popen("netsh wlan show networks").read()
	if ssid in available:
		print('Found')
		break;
conn=os.popen('netsh wlan connect name='+""+ssid+"").read()
print(conn)
