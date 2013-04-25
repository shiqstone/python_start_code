import urllib
import urllib2
import re

class checkPage():
    def __init__(self, domain, num):
        self.domain = domain
        self.num = num
        self.urlList = []#all url list
        self.restList = []#todo list
        self.code = 0#all process count
    def checkA(self, url):
        #data = urllib.open(url)
        data = urllib2.urlopen(url)
        try:
            content = data.read()
        except:
            return False
        self.code += 1
        if(self.restList!=[]):
            self.restList.remove(url)
        filename = "f:/py/temp/"+str(self.code).rjust(5, "0")+".txt"
        f1 = open(filename, "w")
        f1.write(content)
        f1.close()
        #use preg get url href
        p = re.compile('+?',re.I|re.S)
        return p.findall(content)

    def checkUrl(self, content):
        p = re.compile('(|\'<|<)',re.I|re.S)#get url
        m = p.search(content)
        if(m!=None):
            tmpurl = p.search(content).group(3)
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
        url="http://"+self.domain+url
        #remove repeat url
        for n in self.urlList:
            if(url==n):
                return False
        self.urlList.append(url)
        self.restList.append(url)

    def getPage(self, url):
        if(self.code<10):
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
