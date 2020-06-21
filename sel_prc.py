#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:28:12 2020

@author: tianzhu
"""

#import packages
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome("desktop/Python/chromedriver/chromedriver")
driver.get('https://forums.edmunds.com/discussion/56846/land-rover/range-rover-sport/2020-land-rover-range-rover-sport-lease-deals-and-prices')

#get user id
user_element = driver.find_elements_by_xpath('//*[@id="Discussion_56846"]/div/div[1]/div[1]/span[1]/a[2]')[0]
user_id = user_element.text
#get comment date
user_date = driver.find_elements_by_xpath('//*[@id="Discussion_56846"]/div/div[1]/div[2]/span[1]/a/time')[0]
date = user_date.get_attribute('title')
#get comment
user_comment = driver.find_elements_by_xpath('//*[@id="Discussion_56846"]/div/div[2]/div/div[1]')[0]
comment = user_comment.text

#find all ids
//*[@id="Comment_5772188"]/div

ids = driver.find_elements_by_xpath('//*[contains(@id, "Comment_")]')

comment_ids = []

for i in ids:
    comment_ids.append(i.get_attribute('id'))


