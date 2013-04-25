#encoding:UTF-8
'''
@author: ahuaxuan (张荣华)
@date: 2009-02-06
'''
import re
from httplib import HTTPConnection
from datetime import datetime
import urllib
import urllib2
import sys

header = {}
header['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3'
header['Accept-Language'] = 'en-us,en;q=0.7,zh-cn;q=0.3'
header['Accept-Encoding'] = 'UTF-8'
header['Accept-Charset'] = 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
header['Keep-Alive'] = '300'
header['Connection'] = 'keep-alive'
header['Referer'] = 'http://www.weather.com.cn/'

def postData(url, body):  
    
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    req = urllib2.Request(url = url, data = urllib.urlencode(body), headers=header)
    u = urllib2.urlopen(req)
    
    htmlSource = u.read()
   
    return htmlSource

def getData(url):
    
    req = urllib2.Request(url,headers = header)
    res = urllib2.urlopen(req)
    html = res.read()
    
    res.close()
    
    return html

todayPattern = '<div class="box_contenttodayinwea" id="c_1_1">[\s]*?'+\
                '<p>[\s]*?<span>[\s\S]*?</span>[\s]*?' + \
                '<em><strong>(?P<wea>[\s\S]*?)</strong></em>[\s]*?' + \
                '<em class="no_today">(?P<temp>[\s\S]*?)</em>[\s]*?' + \
                '<em>(?P<wind>[\s\S]*?)</em><br/>[\s]*?</p>'
                
futurePattern = '<div class="fut_weatherbox7">[\s]*?' + \
                    '<h3>(?P<date>[\s\S]*?)</h3>[\s]*?'+ \
                    '<p>(?P<aa>[\s\S]*?)</p>[\s]*?'+ \
                    '<h4 class="temp00_dn">(?P<wea>[\s\S]*?)</h4>[\s]*?'+ \
                    '<h4 class="temp01_dn">(?P<tempH>[\s\S]*?)</h4>[\s]*?'+ \
                    '<h4 class="temp02_dn">(?P<tempL>[\s\S]*?)</h4>[\s]*?'+ \
                    '<h4 class="temp03_dn"><a name="sk">(?P<wind>[\s\S]*?)</a></h4>[\s]*?'+ \
                '</div>'

'''
return the json format data of weather
http://search.weather.com.cn/static/url.php
'''
def getWeather(cityName, url):
    body = {}
    body['cityinfo'] = cityName
    text = postData(url, body)
    
    pattern = re.compile("<meta http-equiv=\"refresh\" content=\"0;URL=([\\s\\S]*?)\">")
    rlst = pattern.findall(text)
    
    text = getData(rlst[0])
    fieldList = ['wind', 'wea', 'temp']
    lst = parserWeaPattern(fieldList, text, todayPattern)
    
    fieldList2 = ['wind', 'wea', 'date', 'tempH', 'tempL']
    lst2 = parserWeaPattern(fieldList2, text, futurePattern)
    
    print u"--------------今日天气:-------------".encode("GBK")
    for aa in lst:
        for key,value in aa.items():
            print value
        
    print u"\r\n--------------未来几天:--------------".encode("GBK")
    for aa in lst2:
        print '%s,%s,%s,%s,%s'%(aa['date'],aa['wind'],aa['wea'],aa['tempH'],aa['tempL'])
    return lst

def parserWeaPattern(fieldList, text, pattern):  
    
    list = []
    p = re.compile(pattern)
    iterator = p.finditer(text)
    for matcher in iterator:
        data = {}
        for field in fieldList:
            data[field] = matcher.group(field).encode("GBK")
        list.append(data)
    return list
       
if __name__ == '__main__':
    
    #也可以用区号
    city = u'上海'.encode("GBK")
    reload(sys)
    sys.setdefaultencoding('UTF-8')
    
    print city
    getWeather(city, 'http://search.weather.com.cn/static/url.php')
    
