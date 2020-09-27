# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:57:46 2020

@author: HAN
"""

import bs4 
from selenium import webdriver 
#from URLtoMp3 import TransURLToMp3,MoveFileToFolder
import time
from selenium.webdriver.common.keys import Keys
import youtube_dl
import os
import threading

youtubeLinks={}
#URL to Mp3 轉檔 (存在程式同層)
def TransURLToMp3(URL,ID):
    print("Download Link : ","%s"%URL)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(URL, download=False)
        video_title = info_dict.get('title', None)
    
    #path = f'.\\{video_title}.mp3'
    path = f'.\\{ID}.mp3'
    ydl_opts.update({'outtmpl':path})
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
        print("Success")

def MoveFileToFolder(folderName):
    #將程式同層的mp3 存進MP3_Files
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    os.system('move .\\*.mp3 .\\{folderName}\\')
    print("finish")

def findURL(soup,idCount):
    hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")
    for a in hrefs:
        idCount+=1
        youtubeLinks[idCount]=("https://www.youtube.com/"+a['href'])
        #print(idCount,youtubeLinks[idCount])
        if(youtubeLinks[idCount] in youtubeLinks):
            print("Repeat",youtubeLinks[id])
    return idCount
        
        
def main():
    folderName=string = "old+school+type+beat"
    
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
        #print(urlCount) 

    print("End for Search，Prepare to Download and Trans")
    for key,value in youtubeLinks.items():
        
        try:
            #print(key,value)
            print(key," Now prepare Download")
            threading.Thread(target=TransURLToMp3(value,key)).start()
        except:
            print("Key : ",key," has some Problem Error !! ")
    print("Finished Download ，Excute MoveFile")
    MoveFileToFolder(folderName)
        
main()