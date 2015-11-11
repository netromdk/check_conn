#! /usr/local/bin/python
import time
import requests
import subprocess

connected = True

def notify(msg):
	subprocess.call(["terminal-notifier", "-message", msg])

while(True):
	time.sleep(60)
	try:
		response = requests.get("https://google.com")
		if connected is False:
			notify("Internet connection restored.")
		connected = True
	except:
		if connected is not False:
		  notify("Internet connection dropped.")
		connected = False