#!/usr/bin/env python
# coding=utf8
#
# Copyright (C) 2015, Michiel Sikma
# MIT license.

'''
Script to scrape the SVG country flags from Wikipedia and save them locally.
'''
import requests
import json
import bs4
import os
import urllib2

FLAGS_FILE = 'svg-flags.json'
FLAGS_DIR = './output'

# Create the output directory if it doesn't exist.
if not os.path.exists(FLAGS_DIR):
    os.makedirs(FLAGS_DIR)

# Iterate through a list of flag image pages on Wikipedia.
flags = json.loads(open(FLAGS_FILE).read())

print('Downloading %d flags.' % len(flags))

for flag in flags:
    # Request the Wikipedia image detail page and parse it.
    req = requests.get(flag)
    soup = bs4.BeautifulSoup(req.text)
    
    # Select the <a> tag with the link to the full flag file.
    link = soup.select('div#file > a')[0]['href']
    if link[:5] != 'http:':
        link = 'http:' + link
    
    # Now download it and store it in our output directory.
    filename = FLAGS_DIR + '/' + link.split('/')[-1:][0]
    content = urllib2.urlopen(link)

    print('...`%s\' to `%s\'.' % (link, filename))
    
    file = open(filename, 'wb')
    file.write(content.read())
    file.close()
    break
