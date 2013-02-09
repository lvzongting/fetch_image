#!/usr/bin/env python
#-*- encoding:utf-8 -*-

##ref https://secure.flickr.com/services/api/misc.urls.html
##ref https://secure.flickr.com/services/api/flickr.photos.search.html
##ref https://secure.flickr.com/services/api/explore/flickr.photos.search

import json
import os
import time
import requests
import urllib
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError

def get_img(query, path, img_num):
    """Download full size images from Google image search.
  
    Don't print or republish images without permission.
    I used this to train a learning algorithm.
    """
    
    api_key = '4b6a2f89f249ee3b0f2f1e97eb2254a0' 
    #if meet api_key Error please visit https://secure.flickr.com/services/api/explore/flickr.photos.search  and push the "Call method" button ,and then search api_key in the reply page 
    BASE_URL = 'https://secure.flickr.com/services/rest/?method=flickr.photos.search&format=json&api_key=' + api_key + '&text='+ query.replace(' ','+') +'&per_page=' + str(img_num)

    BASE_PATH = os.path.join(path, query)
  
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
  
    r = requests.get(BASE_URL)
    title=1
    for image_info in json.loads(r.text[14:-1])['photos']['photo']:
       file = os.path.join(BASE_PATH, '%s.jpg') % str(title)
       
       url = 'http://farm' + str(image_info['farm'])  + '.staticflickr.com/' + str(image_info['server']) + '/' + image_info['id'] + '_' + image_info['secret'] + '_b.jpg' 
       try:
           print 'Fetching  %s ' % url 
           urllib.urlretrieve(url, file)
#           os.system('aria2c "' + url + '" -o ' + file)
#           os.system('wget "' + url + '" -O ' + file)
           print 'save as %s' % file
       except ConnectionError, e:
           print 'could not download %s' % url
           continue
       else :
           print 'download %s is uncomplete' % url
           continue

       title += 1

#get_img('query', 'Directory',30)

#The URL takes the following format:
#
#http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
#	or
#http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}_[mstzb].jpg
#	or
#http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{o-secret}_o.(jpg|gif|png)
#
#The letter suffixes are as follows:

#s	small square 75x75
#q	large square 150x150
#t	thumbnail, 100 on longest side
#m	small, 240 on longest side
#n	small, 320 on longest side
#-	medium, 500 on longest side
#z	medium 640, 640 on longest side
#c	medium 800, 800 on longest side†
#b	large, 1024 on longest side*
#o	original image, either a jpg, gif or png, depending on source format
#Example
#
#http://farm1.staticflickr.com/2/1418878_1e92283336_m.jpg
#
#farm-id: 1
#server-id: 2
#photo-id: 1418878
#secret: 1e92283336
#size: m
