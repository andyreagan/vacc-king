#!/usr/bin/python
#
# tweetnewking.py
#
# simply tweet the new VACC king

from sys import argv
import datetime

if __name__ == '__main__':

    tweet='@andyreagan the geo feed is behind one hour as of {0}'.format(datetime.datetime.strftime('%H-%M on %Y-%m-%d',datetime.datetime.now()))
    
    # store the keys somewhere (so I can share this script)
    f = open('keys','r')
    APP_KEY = f.readline().rstrip()
    APP_SECRET = f.readline().rstrip()
    OAUTH_TOKEN = f.readline().rstrip()
    OAUTH_TOKEN_SECRET = f.readline().rstrip()
    f.close()
    
    from twython import Twython, TwythonError
    
    twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    
    try:
      twitter.update_status(status=tweet)
    except TwythonError as e:
      print e






