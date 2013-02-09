#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import json
import os
import time
import requests
import re
import urllib
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError

def get_img(query, path, img_num):
    """Download full size images from Google image search.
  
    Don't print or republish images without permission.
    I used this to train a learning algorithm.
    """
    BASE_URL = "http://bing.com/images/search?q=" + query.replace(' ','+') + "&count=" + str(img_num)   #&first=10 
  
    BASE_PATH = os.path.join(path, query)
  
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
    print 'Fetching index....'
    r = requests.get(BASE_URL)
    p = re.compile('(?<=a href="/images/search\?q=' + query.replace(' ','\+') + '\&amp;view=detail&amp;id=).+?(?=\&amp;FORM=IDFRIR)')
    images_id = p.findall(r.text)
    title=1
    for id in images_id:
        file = os.path.join(BASE_PATH, '%s.jpg') % str(title)

        print 'Fetching image detail...'
        detail = requests.get('http://bing.com/images/search?q=' + query.replace(' ','+') + '&view=detail&id=' + id + '&FORM=IDFRIR')  
        p =re.compile('(?<=<a id="m_fsi" href=").+?(?=" target)') 
        url = str(p.findall(detail.text)[0])

        try:
            print 'Fetching %s' % url
            urllib.urlretrieve(url, file)
#            os.system('aria2c "' + url + '" -o ' + file)
#            os.system('wget "' + url + '" -O ' + file)
#            print 'wget "' + url + '" -O ' + file
            print 'save as %s' % file
        except ConnectionError, e:
            print 'could not download %s' % url
            continue
        else :
            print 'download %s is uncomplete' % url
            continue  

        title += 1
  
# Example use
#go(query, Directory,10)

