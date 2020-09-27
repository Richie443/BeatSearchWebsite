# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:57:46 2020

@author: HAN
"""

from __future__ import unicode_literals
import bs4 
from selenium import webdriver 
#from URLtoMp3 import TransURLToMp3,MoveFileToFolder
import time
from selenium.webdriver.common.keys import Keys
import youtube_dl
import os
import threading

youtubeLinks={}

def TransURLToMp3(URL,ID):
# =============================================================================
#     #URL to Mp3 轉檔 (存在程式同層)
# =============================================================================
    print("Download Link : ","%s"%URL)
    ydl_opts = {                            #mp3的一些要求格式
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:   #設定 youtube_dl套件 需要的格式內容
        info_dict = ydl.extract_info(URL, download=False)
        video_title = info_dict.get('title', None)
    
    #path = f'.\\{video_title}.mp3'
    path = f'.\\{ID}.mp3'                       #存放路徑(在程式同層的資料夾下面)
    ydl_opts.update({'outtmpl':path})           #存放路徑(在程式同層的資料夾下面)
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: #開始下載
        ydl.download([URL])
        print("Success")



def MoveFileToFolder(folderName):
# =============================================================================
#     #將程式同層的mp3 存進MP3_Files
# =============================================================================
    if not os.path.exists(folderName):          #檢查有無過新增資料夾
        os.mkdir(folderName)
    os.system('move .\\*.mp3 .\\{folderName}\\') #把跟程式同層的.mp3黨 存進 資料夾裡
    print("finish")



def findURL(soup,idCount):          
# =============================================================================
#   分析soup裏頭的資料(從beautifulsoup爬完後下載回傳的) 找出所有的連結網址，存
#   進 youtubelinks裡(一個字典變數)
# =============================================================================
    hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")  #設定只要url的格式要求
    for a in hrefs:  #把url存進 變數裡
        idCount+=1
        youtubeLinks[idCount]=("https://www.youtube.com/"+a['href']) #新增dict 的key,value (類似array的 append)
        #print(idCount,youtubeLinks[idCount])
        if(youtubeLinks[idCount] in youtubeLinks):
            print("Repeat",youtubeLinks[id])
    return idCount
        
        
def main():
    folderName=string = "trap+type+beat"                        #設定搜尋關鍵字
    url = "https://www.youtube.com/results?search_query=" + string #youtube+關鍵字
    
    browser = webdriver.Chrome()        #開啟chrome
    browser.get(url)                    #輸入網址並搜尋
    urlCount=0
    
    
    while(urlCount<100):                #持續爬蟲 直到搜尋到的url超過100個
        #height = browser.execute_script("return document.body.scrollHeight")   #找出網站捲動的最底下
        time.sleep(1)                                                       #等待網頁內容加載
        browser.find_element_by_tag_name('body').send_keys(Keys.END)        #滾動網頁到最底下
        
    #    if int(height)==0:
    #        break
        source = browser.page_source                                        #返回網站原始htmlcode內容
        soup = bs4.BeautifulSoup(source,'html.parser')                      #用beautifulSoup解析出domTree格式(變成平常我們看到的樣子)
        urlCount=findURL(soup,urlCount)                                     #找出html裡的url網址
        #print(urlCount) 

    print("End for Search，Prepare to Download and Trans")
    for key,value in youtubeLinks.items():                                  #把所有的url下載下來並轉檔
        
        try:
            #print(key,value)
            print(key," Now prepare Download")
            threading.Thread(target=TransURLToMp3(value,key)).start()       #下載url
        except:
            print("Key : ",key," has some Problem Error !! ")   
    print("Finished Download ，Excute MoveFile")
    MoveFileToFolder(folderName)
    
        
main()