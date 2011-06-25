#!/usr/bin/env python

import os, sys

sys.path.append("deps/httplib2-0.7.1")
sys.path.append("deps/python-oauth2")
sys.path.append("deps/simplejson-2.1.6")
sys.path.append("deps/python-twitter-0.8.2")

import twitter

api = twitter.Api()

# twitter url => twitter id

artist_twitterid = []

for line in sys.stdin:
    line = line.strip()
    artist, username = line.split('\t')
    tid = api.GetUser(username).id
    artist_twitterid.append((artist, tid))

for artist, tid in artist_twitterid:
    print '%s\t%s'% (artist, tid)

