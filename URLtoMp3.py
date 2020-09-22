# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:57:14 2020

@author: HAN
"""

from __future__ import unicode_literals
import youtube_dl
import os


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

def MoveFileToFolder():
    #將程式同層的mp3 存進MP3_Files
    if not os.path.exists('MP3_Files'):
        os.mkdir('MP3_Files')
    os.system('move .\\*.mp3 .\\MP3_Files\\')
    print("finish")