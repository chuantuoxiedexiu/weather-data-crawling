#-*-coding:utf-8 -*-
from lxml import etree
import json
import sys
import time
import urllib
from selenium import webdriver
import re
reload(sys)
sys.setdefaultencoding('utf8')

def crawl_weather():
    f=open('.\\city_with_checkin.txt','r')
    content=f.readlines()
    f.close()
    city_list=[]
    for each in content:
        city_list.append(each.strip('\n'))
    for i in range(388,len(city_list)):
        data=[]
        city=city_list[i]
        year=['2011','2012','2013','2014','2015']
        month=['01','02','03','04','05','06','07','08','09','10','11','12',]
        #year=['2011','2012']
        #month=['01','02']
        failure=0
        for y in year:
            #print y
            for m in month:
                if failure==1:
                    continue
                response=urllib.urlopen('http://lishi.tianqi.com/'+city+'/'+y+m+'.html')
                time.sleep(1)
                #print response.geturl()
                if len(response.info())!=13:
                    content=response.read()
                    tree=etree.HTML(content)
                    a=tree.xpath('//div[@class="tqtongji2"]/ul')
                    print '*'*1,i,' / ',len(city_list),city_list[i], y,m,len(a),'*'*1
                    for b in a[1:]:
                        #data.append([])
                        c=b.xpath('./li//text()')
                        #print c[0],c[1],c[2],c[3],c[4],c[5]
                        #for d in c:
                        #    print d[0:],
                        #    data[-1].append(d[0:])
                        #print
                        data.append(c)
                        #print c[0]
                    #print len(a)
                else:
                    failure=1
                    continue
                
        if failure==0:
            f=open('.\\weather_data\\'+city_list[i]+'.txt','w')
            f.write('日期,最高气温,最低气温,天气,风向,风力\n')
            for each in data:
                aa=''
                for cc in each:
                    aa+=(cc+',')
                aa=aa.strip(',')
                f.write(aa+'\n')
            f.close()
                    
if __name__=='__main__':
    crawl_weather()
