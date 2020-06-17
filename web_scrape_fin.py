#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:11:51 2020

@author: tianzhu
"""

#install package
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = 'https://www.bloomberg.com/news/articles/2020-06-17/u-s-trade-chief-downplays-prospect-of-2020-deals-with-u-k-eu?srnd=economics-vp'
web_prc = ureq(my_url)
#open up connection, grabbing contents from web
page_html = web_prc.read()
web_prc.close()
#html parse
page_soup = soup(page_html,"html.parser")
page_soup
containers = page_soup.findAll("div",{"class","item-container"})


#get contents from web
# r1 = requests.get('https://www.bloomberg.com/news/articles/2020-06-17/u-s-trade-chief-downplays-prospect-of-2020-deals-with-u-k-eu?srnd=economics-vp')
# coverpage = r1.content

#create soup
soup1 = soup(coverpage, 'html.parser')
soup1
coverpage_news = soup1.findAll("article", {"class":"WSJTheme"})
coverpage_news[0]
len(coverpage_news)
