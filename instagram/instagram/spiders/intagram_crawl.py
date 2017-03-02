import json
import scrapy
import MySQLdb
import time
import datetime
import urllib

from array import *
from kafka import KafkaProducer, KafkaConsumer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.http import TextResponse
from pyvirtualdisplay import Display

class Instagram(scrapy.Spider):
    # pdb.set_trace()
    name = "insta"
    allowed_domains = ["https://www.instagram.com"]
    start_urls = ["https://www.instagram.com"]

    def __init__(self):
        # self.connect = self.conn
        # path_to_chromedriver = 'D://chromedriver'
        # path = 'C://Program Files//Mozilla Firefox//firefox'
        # path_to_chromedriver='/usr/local/bin/chromedriver'
        # driver = webdriver.Chrome(executable_path=path_to_chromedriver)
        # display = Display(visible=0, size=(800, 600))
        # display.start()

        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1280,720)
        # driver = webdriver.PhantomJS()

    def start_requests(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//div[@class="_p8ymb"]/div[2]/p/a').click()
        except Exception, e:
            print e
        id = self.driver.find_element_by_xpath('//div[@class = "_uikn3"]/form/div/input')
        id.click()
        time.sleep(2)
        id.send_keys("yudhaaulia15@yahoo.com")
        time.sleep(3)
        password = self.driver.find_element_by_xpath('//div[@class = "_uikn3"]/form/div[2]/input')
        password.click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[@role='dialog']/button").click()
        except Exception, e:
            print e
        password.send_keys("yuliapi2016")
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class = "_uikn3"]/form/span/button').click()
        time.sleep(5)
        # import pdb;pdb.set_trace()
        try:
            self.driver.find_element_by_xpath('//div[@class="_n3cp9"]/div/button').click()
            time.sleep(3)
        except Exception, e:
            print e
        search = self.driver.find_element_by_xpath('//div[@class="_t1y9a _98hun"]/div')
        search.click()
        time.sleep(2)
        f_search = self.driver.find_element_by_xpath('//div[@class="_9pxkq _icv3j"]/input')
        f_search.send_keys("tahilalats")
        time.sleep(2)
        f_search.send_keys(Keys.ENTER)
        time.sleep(2)
        response = TextResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
        pp = response.xpath('//main[@role="main"]/article/header/div/img/@src').extract()
        pp = ''.join(pp).encode('utf-8')
        nama = "midil"
        direktori = 'C:\Users\EB-NB19\Documents\pict\ ' + nama + '.jpg'
        urllib.urlretrieve(pp, direktori)
        # import pdb;pdb.set_trace()
        count = 1
        for a in range(1, 100):
            for i in range(1, 3):
                count +=1
                # import pdb;pdb.set_trace()
                response = TextResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
                try:
                    ins = response.xpath('//main[@role="main"]/article/div/div/div[' + str(a) + ']/a[' + str(i) + ']/div/div/img').extract()
                    ins = ''.join(ins).encode('utf-8')
                    img = ins.split("src")[1]
                    img = img.split("?")[0]
                    img = img.split('"')[1]
                except Exception, e:
                    print e
                nama = "midil"+str(count)
                direktori = 'C:\Users\EB-NB19\Documents\pict\ ' + nama + '.jpg'
                urllib.urlretrieve(img, direktori)
                time.sleep(1)
                try:
                    load = response.xpath('//main[@role="main"]/article/div/div[3]/a/text()').extract()
                except Exception, e:
                    print e
                load = ''.join(load).encode('utf-8')
                if load == "Load more":
                    self.driver.find_element_by_xpath('//main[@role="main"]/article/div/div[3]/a').click()
                else:
                    pass
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body').send_keys(Keys.END)
                time.sleep(2)
                self.driver.find_element_by_xpath('/html/body').send_keys(Keys.END)
                time.sleep(2)
        # response = TextResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
        # try:
        #     name = response.xpath('//main[@role="main"]/article/header/div[2]/div/h1/text()').extract()
        # except Exception, e:
        #     print e
        # name = ''.join(name).encode('utf-8')
        # try:
        #     desc = response.xpath('//main[@role="main"]/article/header/div[2]/div[2]/text()').extract()
        # except Exception, e:
        #     print e
        # desc = ''.join(desc).encode('utf-8')
        # try:
        #     post = response.xpath('//div[@class="_de9bg"]/ul/li/span/span/text()').extract()
        # except Exception, e:
        #     print e
        # post = ''.join(post).encode('utf-8')
        # try:
        #     follower = response.xpath('//div[@class="_de9bg"]/ul/li[2]/a/span/@title').extract()
        # except Exception, e:
        #     print e
        # follower = ''.join(follower).encode('utf-8')
        # try:
        #     following = response.xpath('//div[@class="_de9bg"]/ul/li[3]/a/span/text()').extract()
        # except Exception, e:
        #     print e
        # following = ''.join(following).encode('utf-8')
        # # print "=========================="
        # # print nama
        # print "=========================="
        # print name
        # print "=========================="
        # print desc
        # print "=========================="
        # print post
        # print "=========================="
        # print follower
        # print "=========================="
        # print following
        # print "=========================="
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//div[@class="_de9bg"]/ul/li[2]/a').click()
        # time.sleep(2)
        # f1 = 0
        # # import pdb;pdb.set_trace()
        # self.driver.find_element_by_xpath('//div[@role="dialog"]/div[2]/div/div[2]/ul/li/div/div/div/div').click()
        # time.sleep(2)
        # for fol in range(1, 1000000000):
        #     f1 +=1
        #     response = TextResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
        #     folcount = response.xpath('//div[@role="dialog"]/div[2]/div/div[2]/ul/li[' + str(fol) + ']/div/div/div/div/a/text()').extract()
        #     time.sleep(1)
        #     folcount = ''.join(folcount).encode('utf-8')
        #     if folcount == "":
        #         break
        #     else:
        #         print "=========================="
        #         print f1
        #         print "=========================="
        #         print folcount
        #         print "=========================="
        #     self.driver.find_element_by_xpath('//div[@role="dialog"]/div[2]/div/div[2]/ul/li/div/div/div/div').send_keys(Keys.PAGE_DOWN+Keys.PAGE_DOWN+Keys.PAGE_DOWN+Keys.PAGE_DOWN+Keys.PAGE_DOWN)
        #     time.sleep(1)
        # self.driver.find_element_by_xpath('//div[@role="dialog"]').send_keys(Keys.ESCAPE)
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//div[@class="_de9bg"]/ul/li[3]/a').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//div[@role="dialog"]/div[2]/div/div[2]/ul/li/div/div/div/div').click()
        # time.sleep(1)
        # f2 = 0
        # for fol2 in range(1, 100000000):
        #     f2 +=1
        #     response = TextResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
        #     folcount = response.xpath('//div[@role="dialog"]/div[2]/div/div[2]/ul/li[' + str(fol2) + ']/div/div/div/div/a/text()').extract()
        #     time.sleep(1)
        #     folcount = ''.join(folcount).encode('utf-8')
        #     if folcount == "":
        #         break
        #     else:
        #         print "=========================="
        #         print f2
        #         print "=========================="
        #         print folcount
        #         print "=========================="
        #     self.driver.find_element_by_xpath('//div[@role="dialog"]/div[2]/div/div[2]/ul/li/div/div/div/div').send_keys(Keys.PAGE_DOWN+Keys.PAGE_DOWN+Keys.PAGE_DOWN+Keys.PAGE_DOWN+Keys.PAGE_DOWN)
        #     time.sleep(1)
        # self.driver.find_element_by_xpath('//div[@role="dialog"]').send_keys(Keys.ESCAPE)
        # time.sleep(2)