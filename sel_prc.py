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
ids = driver.find_elements_by_xpath('//*[contains(@id, "Comment_")]')

comment_ids = []

for i in ids:
    comment_ids.append(i.get_attribute('id'))

print(comment_ids)


ids_ = []
dates = []
comments = []

for ids in comment_ids:
    user_ids = driver.find_elements_by_xpath(f'//*[@id="{ids}"]/div/div[2]/div[1]/span[1]/a[2]')[0]
    ids_.append(user_ids.text)
    
    user_dates = driver.find_elements_by_xpath(f'//*[@id="{ids}"]/div/div[2]/div[2]/span/a/time')[0]
    dates.append(user_dates.get_attribute('title'))
    
    user_comments = driver.find_elements_by_xpath(f'//*[@id="{ids}"]/div/div[3]/div/div[1]')[0]
    comments.append(user_comments.text)
    
comments_ = pd.DataFrame({'Dates':dates, 
                          'ID':ids_, 
                          'Comments':comments})

print(comments_.dtypes)
print(comments_)
comments_['Dates'] = comments_['Dates'].astype(str)
comments_['ID'] = comments_['ID'].astype(str)
comments_['Comments'] = comments_['Comments'].astype(str)
comments_.to_csv('car_comments.csv')

