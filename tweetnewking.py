#!/usr/bin/python
#
# tweetnewking.py
#
# simply tweet the new VACC hogger

from sys import argv
king = argv[1]
jobs = argv[2]

tweet='all hail the newest VACC king!! '+king+' has '+jobs+' jobs out there!'

# store the keys somewhere (so I can share this script)
f = open('keys.txt','r')
APP_KEY = f.readline()
APP_SECRET = f.readline()
OAUTH_TOKEN = f.readline()
OAUTH_TOKEN_SECRET = f.readline()
f.close()

from twython import Twython, TwythonError

twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

try:
  twitter.update_status(status=tweet)
except TwythonError as e:
  print e
