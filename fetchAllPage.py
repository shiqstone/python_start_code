import urllib
import urllib2
import re
import os

class checkPage():
    def __init__(self, domain, num):
        self.domain = domain
        self.num = num
        self.urlList = []#all url list
        self.restList = []#todo list
        self.code = 0#all process count
    def checkA(self, url):
        #data = urllib.open(url)
        print url
        data = urllib2.urlopen(url)
        try:
            content = data.read()
        except:
            return False
        self.code += 1
        if(self.restList!=[]):
            self.restList.remove(url)
        #filename = "./temp/"+str(self.code).rjust(5, "0")+".txt"
        refurl = re.sub(self.domain+'(.*?)', r'\1', url)
        if(re.match(r'^\/php.*?|[^/]', refurl)):
            if("/php/"==refurl):
                filename="./temp/php/index.html"
            elif(re.match(r'[^/]', refurl)):    
                filename = "./temp/php/"+refurl
            else:
                filename = "./temp"+refurl
            path = os.path.dirname(filename)
            #basename = os.path.dirname(filename)
            if(not os.path.exists(path)):
                os.makedirs(path)
            f1 = open(filename, "w+")
            f1.write(content)
            f1.close()
            #use preg get url href
            #p = re.compile('+?',re.I|re.S)
            p = re.compile('<a.*?href=.*?<\/a>',re.I|re.S)
            return p.findall(content)
        else:
            return ""

    def checkUrl(self, content):
        #import pdb
        #pdb.set_trace()
        p = re.compile('href=\".*?\"', re.I|re.S)
        u = p.findall(content)
        m = re.sub('href="(.*?)"', r'\1', u[0])
        #p = re.compile('(|\'<|<)',re.I|re.S)#get url
        #m = p.search(content)
        if(m!=None):
            #tmpurl = p.search(content).group(3)
            tmpurl = m
        else:
            tmpurl = ""
        if(tmpurl!=""):
            self.checkSame(tmpurl)

    def checkSame(self, url):
        if(url=="#"):
            return False
        if(url.find("mailto:")!=-1 or url.find("(")!=-1):
            return False
        if(url.find("http://")!=-1):
            if(url.find(self.domain)!=-1):
                p=re.compile("http://.*?"+self.domain, re.l)
                p.sub("", url)
            else:
                return False
        if(re.match(r'[^/]', url)):
            url = "/php/"+url
        url=self.domain+url
        #remove repeat url
        for n in self.urlList:
            if(url==n):
                return False
        self.urlList.append(url)
        self.restList.append(url)

    def getPage(self, url):
        if(self.code<300):
            m = self.checkA(url)
            for n in m:
                self.checkUrl(n)
            return 1
        else:
            return 0

c = checkPage("http://www.w3school.com.cn", 0)
c.getPage("http://www.w3school.com.cn/php/")

while(1==1):
    if(c.urlList==[]):break
    for r in c.restList:
        if(c.getPage(r)==0):break
