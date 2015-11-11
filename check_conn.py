#!/usr/bin/env python
import time
import requests
import subprocess

SITE = "https://google.com"
TIMEOUT = 30 # seconds

def notify(msg):
  subprocess.call(["terminal-notifier", "-message", msg])

if __name__ == "__main__":
  connected = True

  while True:
    time.sleep(TIMEOUT)
    try:
      response = requests.get(SITE)
      if connected is False:
        notify("Internet connection restored.")
        connected = True
    except:
      if connected is not False:
        notify("Internet connection dropped.")
        connected = False
