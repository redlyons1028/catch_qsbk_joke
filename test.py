# -*- coding:utf-8 -*-
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(
        '<div.*?author.*?<a.*?<a.*?h2>(.*?)</h2>.*?<a.*?contentHerf.*?span>(.*?)</span>.*?'+
        '-->(.*?)<div class="stats.*?number.*?>(.*?)</i>',
        re.S)
    items = re.findall(pattern, content)

    photoPattern = re.compile('<a.*?src="(.*?)".*?',re.S)
    for item in items:
        haveImg = re.search("img",item[2])
        if not haveImg:
            print item[0],item[1],'none',item[3]
        else:
            photo_url = re.findall(photoPattern, item[2])
            print item[0],item[1],photo_url[0],item[3]
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason