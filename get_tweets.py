# -*- coding: utf-8 -*-
"""
Created on Sun May 24 09:48:05 2015

@author: u3kil
"""

from TwitterAPI import TwitterAPI
from configparser import SafeConfigParser

"""
Create twitter connection via TwitterAPI
"""
cfile = open('tweet_analysis.config','r')
config = SafeConfigParser()
config.readfp(cfile)

CONSUMER_KEY = config.get('keys','CONSUMER_KEY')
CONSUMER_SECRET = config.get('keys','CONSUMER_SECRET')
ACCESS_TOKEN_KEY = config.get('keys','ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = config.get('keys','ACCESS_TOKEN_SECRET')

api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

"""
Get tweets using a subject filter
"""

t = api.request('statuses/filter', {'track':'happy'})
for s in t:
    print(s['text'] if 'text' in s else s)
