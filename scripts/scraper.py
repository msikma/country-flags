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
import sys
import urllib2

COUNTRIES_FILE = 'flags-remote.json'
OUTPUT_DIR = '../flags/svg'

# Create the output directory if it doesn't exist.
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Iterate through a list of flag image pages on Wikipedia.
countries = json.loads(open(COUNTRIES_FILE).read())

print('Downloading %d flags.' % len(countries))

for c_code in countries:
    # Request the Wikipedia image detail page and parse it.
    country = countries[c_code]
    req = requests.get(country['url'])
    soup = bs4.BeautifulSoup(req.text)
    
    # Select the <a> tag with the link to the full flag file.
    link = soup.select('div#file > a')[0]['href']
    if link[:5] != 'http:':
        link = 'http:' + link
    
    # Now download it and store it in our output directory.
    out_fn = c_code.lower() + '.svg'
    out_path = OUTPUT_DIR + '/' + urllib2.unquote(out_fn.encode('utf-8'))
    out_path = unicode(out_path, 'utf-8')
    content = urllib2.urlopen(link).read()
    
    print('...`%s\' for %s.' % (out_path, country['name']))
    
    file = open(out_path, 'wb')
    file.write(content)
    file.close()

# All done.
