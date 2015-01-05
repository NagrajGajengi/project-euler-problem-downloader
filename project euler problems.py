#-------------------------------------------------------------------------------
# Name:         Project Euler Problem Downloader
# Purpose:      Educational
#
# Author:       Nagraj Gajengi
#
# Created:      1/3/2015   
#-------------------------------------------------------------------------------

import urllib2
from BeautifulSoup import BeautifulSoup 
def imgDownloader(i,url,cname):
        usock = urllib2.urlopen(url)                                  
        file_name=cname+" "+str(i)+".gif"
        f = open(file_name, 'wb')                                     
        file_size = int(usock.info().getheaders("Content-Length")[0]) 
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
         
        downloaded = 0
        block_size = 8192                                            
        while True:
                buff = usock.read(block_size)
                if not buff:                                             
                        break
                downloaded = downloaded + len(buff)
                f.write(buff)
        f.close()
def mainF():
    url="https://projecteuler.net/show=all"
    print "Hi"
    page=urllib2.urlopen(url).read()
    print "fetch"
    i=0
    while(True):
        i=i+1
        print str(i)+")",
        start_link=page.find("<h3>")
        if(start_link==-1):
            return
        page=page[start_link+4:]
        pHeadStart=page.find(">")
        pHeadEnd=page.find("</a>")
        pHeading=page[pHeadStart+1:pHeadEnd]
        end_link=page.find("</div>")
        data=page[pHeadEnd:end_link]
        #formatting data
        data=data.replace("</p>","\n")
        data=data.replace("</a>","\n")
        data=data.replace("<br />","\n")
        data=data.replace("&times;","X")
        data=data.replace("&lt;"," < ")
        plink="Link=https://projecteuler.net/problem="+str(i)
        filename="problem - "+str(i)
        Ffilename=filename+".txt"
        f = open(Ffilename, 'w+')
        f.write(plink)
        f.write("\n")
        f.write(pHeading)
        f.write("\n")
        soup= BeautifulSoup(data)
        cleantext = soup.text
        f.write(cleantext.encode('utf8'))
        soup= BeautifulSoup(data)
        tags=soup.findAll('img')
        a=set(tag['src'] for tag in tags)
        t=0
        for p in a:
            t=t+1
            imgDownloader(t,"https://projecteuler.net/"+p,filename)
        if(t!=0):
            f.write("Refer Image(s)")
        f.close()
        print "Problem "+str(i)+" Done"
mainF()
