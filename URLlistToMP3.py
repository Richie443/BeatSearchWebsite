from pytube import YouTube
from selenium import webdriver
from moviepy.editor import *
import requests
import bs4


html = "https://www.youtube.com/playlist?list=PL_LLhF5u_RaAUrmLS7jO4X9t42tUPKPNE"
browser = webdriver.Chrome('D:\Desktop\chromedriver.exe')
browser.get(html)

source = browser.page_source
#print(source)
soup = bs4.BeautifulSoup(source,'html.parser')

container = soup.find_all("span", class_="style-scope ytd-playlist-video-renderer")
hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")
base = "https://www.youtube.com"
URLlist = []
id = 0
#file = open("YoutubeURL_chillBeat2.txt","w")
for a in hrefs:
    temp = base + a['href']
    name = YouTube(temp).streams.first().download()
    print(name)
    video=VideoFileClip(name)
    video.audio.write_audiofile(str(id) + '.mp3')
    id+=1
    #print(id)

print("finish")

    