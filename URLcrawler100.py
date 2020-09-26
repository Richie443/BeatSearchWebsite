# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:57:46 2020

@author: HAN
"""

import bs4 
from selenium import webdriver 
from URLtoMp3 import TransURLToMp3,MoveFileToFolder
import time
from selenium.webdriver.common.keys import Keys

youtubeLinks={}
def findURL(soup,idCount):
    hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")
    for a in hrefs:
        idCount+=1
        youtubeLinks[idCount]=("https://www.youtube.com/"+a['href'])
        print(idCount,youtubeLinks[idCount])
        if(youtubeLinks[idCount] in youtubeLinks):
            print("Repeat",youtubeLinks[id])
    return idCount
        
        
def main():
    string = "pop+beat";
    
    url = "https://www.youtube.com/results?search_query=" + string
    
    browser = webdriver.Chrome()
    browser.get(url)
    urlCount=0
    
    
    while(urlCount<100):
        height = browser.execute_script("return document.body.scrollHeight")
        time.sleep(1)
        browser.find_element_by_tag_name('body').send_keys(Keys.END)
        
    #    if int(height)==0:
    #        break
        source = browser.page_source
        soup = bs4.BeautifulSoup(source,'html.parser')
        urlCount=findURL(soup,urlCount)
        print(urlCount) 

    print("End for Search，Prepare to Download and Trans")
    for key,value in youtubeLinks.items():
        TransURLToMp3(value,key)
    print("Finished Download ，Excute MoveFile")
    MoveFileToFolder()
        
main()