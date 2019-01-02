#-*- coding: utf-8 -*-

import urllib2
import re
import socket

#ZH_url = "http://china.chinadaily.com.cn/node_1143902_(page_num).htm"
#E_url = "http://www.chinadaily.com.cn/china/governmentandpolicy/page_(page_num).html"

'''
该函数的作用是 爬取列表中2-102页（共101页）的中文新闻内容
'''
def spider_ZH():

    socket.setdefaulttimeout(5)
    #记录中文文档编号
    news_ZH_org_num = 1

    #遍历新闻100个列表页面
    for i in range(2, 55):
        # 从新闻列表页面获取单个新闻页面的url
        request = urllib2.Request("http://china.chinadaily.com.cn/node_1143902_"+str(i)+".htm")#构建请求（可以添加data,header参数）
        # 放到异常捕获中
        try:
            response = urllib2.urlopen(request, timeout=10)  # 返回一个response对象
            content = response.read().decode('utf-8')  # 返回获取到的网页内容
        except urllib2.HTTPError, e:
            print e.code
            continue
        except urllib2.URLError, e:
            print e.reason
            continue
        except socket.timeout:
            print "time out"
            continue
        pattern = re.compile('<h3><a href="(.*?)" target="_blank" atremote="1">.*?</a></h3>', re.S)
        items = re.findall(pattern, content)
        for item in items:
            #从新闻页面中爬去文章内容
            request2 = urllib2.Request(item)  # 构建请求（可以添加参数）
            #放到异常捕获中
            try:
                response2 = urllib2.urlopen(request2, timeout=10)# 返回一个response对象
                content2 = response2.read().decode('utf-8')  # 返回获取到的网页内容
            except urllib2.HTTPError, e:
                print e.code
                continue
            except urllib2.URLError, e:
                print e.reason
                continue
            except socket.timeout:
                print "time out"
                continue
            pattern2 = re.compile('<h1 class="dabiaoti">(.*?)</h1>.*?<div.*?id="Content".*?>(.*?)</div>', re.S)
            items2 = re.findall(pattern2, content2)
            for item2 in items2:
                dr = re.compile(r'<[^>]+>', re.S)
                dd = dr.sub('', item2[0]) #存入标题
                dd2 = dr.sub('', item2[1]) #存入文章内容
                f = open(r'data/ZH_Org/News_'+str(news_ZH_org_num)+'_Org_ZH.txt', 'w')
                f.write(dd.encode("utf8"))
                f.write(dd2.encode("utf8"))
                f.close()
                print ("中文文章"+str(news_ZH_org_num)+"抓取完毕"+" 此时为第"+str(i)+"页")
                news_ZH_org_num = news_ZH_org_num+1
    return
'''
该函数的作用是爬取新闻列表中1-100页的英文新闻内容
'''
def spider_E():

    # 记录英文文档编号
    news_E_org_num = 1

    # 遍历新闻100个列表页面
    for i in range(1, 55):
        # 从新闻列表页面获取单个新闻页面的url
        request = urllib2.Request("http://www.chinadaily.com.cn/china/governmentandpolicy/page_" + str(i) + ".html")  # 构建请求（可以添加data,header参数）
        # 放到异常捕获中
        try:
            response = urllib2.urlopen(request, timeout=10)  # 返回一个response对象
            content = response.read().decode('utf-8')  # 返回获取到的网页内容
        except urllib2.HTTPError, e:
            print e.code
            continue
        except urllib2.URLError, e:
            print e.reason
            continue
        except socket.timeout:
            print "time out"
            continue
        pattern = re.compile('<h4><a target="_blank" shape="rect" href="(.*?)">.*?</a></h4>', re.S)
        items = re.findall(pattern, content)
        for item in items:
            # 从新闻页面中爬去文章内容
            request2 = urllib2.Request("http:"+item)  # 构建请求（可以添加参数）
            # 放到异常捕获中
            try:
                response2 = urllib2.urlopen(request2, timeout=10)  # 返回一个response对象
            except urllib2.HTTPError, e:
                print e.code
                continue
            except urllib2.URLError, e:
                print e.reason
                continue
            content2 = response2.read().decode('utf-8')  # 返回获取到的网页内容
            pattern2 = re.compile('<div.*?id="lft-art">.*?<h1>(.*?)</h1>.*?<div.*?id="Content".*?>(.*?)</div>', re.S)
            items2 = re.findall(pattern2, content2)
            for item2 in items2:
                dr = re.compile(r'<[^>]+>', re.S)
                dd = dr.sub('', item2[0])  # 存入标题
                dd2 = dr.sub('', item2[1])  # 存入文章内容
                f = open(r'data/E_Org/News_' + str(news_E_org_num) + '_Org_E.txt', 'w')
                f.write(dd.encode("utf8"))
                f.write(dd2.encode("utf8"))
                f.close()
                print ("英文文章" + str(news_E_org_num) + "抓取完毕" + " 此时i为" + str(i))
                news_E_org_num = news_E_org_num + 1
    return
spider_ZH()
spider_E()