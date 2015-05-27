# -*- coding: utf-8 -*-
"""
Created on Sun May 24 09:48:05 2015

@author: u3kil
"""

from TwitterAPI import TwitterAPI
from configparser import SafeConfigParser
from textblob import TextBlob

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

f = open('tweets.txt','w', encoding='utf-8')

t = api.request('statuses/filter', {'track':'happy'})
i = 0
for i in range(100):       ## TEST CODE- Only print first 100 tweets
	for s in t.get_iterator():
		text = TextBlob(s['text'])
		f.write(s['user']['screen_name']+': ' + s['text'] +' '+ str(text.sentiment.polarity) + '\n')
		i+=1
		break
f.close()

