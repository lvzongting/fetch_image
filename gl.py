#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError

def get_img(query, path, img_num):
    """Download full size images from Google image search.
  
    Don't print or republish images without permission.
    I used this to train a learning algorithm.
    """
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + query + '&start=%d'
  
    BASE_PATH = os.path.join(path, query)
  
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
  
    start = 0 # Google's start query string parameter for pagination.
    while start < img_num: # Google will only return a max of 56 results.
       r = requests.get(BASE_URL % start)
       i=1
       for image_info in json.loads(r.text)['responseData']['results']:
           title = start + i
           if title > img_num:
               break
           file = os.path.join(BASE_PATH, '%s.jpg') % str(title)
           
           url = image_info['unescapedUrl']
           try:
               print 'Fetching %s' % url
#              os.system('aria2c "' + url + '" -o ' + file)
               os.system('wget "' + url + '" -O ' + file)
               print 'save as %s' % file
           except ConnectionError, e:
               print 'could not download %s' % url
               continue
  
           i += 1
  
       start += 4 # 4 images per page.
  
       # Be nice to Google and they'll be nice back :)
       time.sleep(1.5)

# Example use
#go('landscape', 'myDirectory')
