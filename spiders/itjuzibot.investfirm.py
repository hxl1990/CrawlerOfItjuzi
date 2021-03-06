#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from itjuzi.items import ItjuziItem
class ItjuziSpider(scrapy.Spider):
	name = "itjuzi"
	allowed_domains = ["itjuzi.com"]
	start_urls = [
		"https://www.itjuzi.com/investfirm?page=%d" %n for n in range(1,646)
    	]
	

	headers = {
    	"Accept": "*/*",
    	"Accept-Encoding": "gzip,deflate",
    	"Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
	"Connection": "keep-alive",
	"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
   	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    	"Referer": "http://www.itjuzi.com/"
    	}


	def parse(self, response):
	        l = ItemLoader(item = ItjuziItem(),response=response)
		l.add_xpath('link',"//p[@class='title']//@href")
		return l.load_item()
#			for x,y,z in zip(item["title"],item["link"],item["desc"]):
#				print x.encode("utf-8") = item["title"],y.encode("utf-8"),z.encode("utf-8") 
