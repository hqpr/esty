#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'o.dubnyak'
__version__ = 1.0

"""
https://github.com/geduldig/TwitterAPI
https://dev.twitter.com/docs/api/1.1

https://hootsuite.com/developers/api/oauth2

consumer_key = "IqoIbOEZn4MVJJ5DePtvA"
consumer_secret = "MLdKfOS65GN7gDn5XSJyO9sjgGdcK1rUZMuLW2uPZg"
access_token_key = "23428449-GU5Ecm0gPC24kYDiC9xPLff0JvUd3LvHBwn7JOZGs"
access_token_secret = "XedJlYAc29XTAOiBjVMVueHJMbYPUzpL8alC9ID4A"

"""
from TwitterAPI import TwitterAPI
import time
import csv

reader = csv.reader(open('keys.csv', 'rb'), delimiter=';', quotechar='"')

for row in reader:
    consumer_key = row[0]
    consumer_secret = row[1]
    access_token_key = row[2]
    access_token_secret = row[3]

    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    msg = ['test', 'is', 'this']

    for m in msg:
        r = api.request('statuses/update', {'status': m})
        time.sleep(5)
        print r.status_code



