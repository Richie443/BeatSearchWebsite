import bs4 
from selenium import webdriver 
import URLtoMp3
string = "pop+beat";

url = "https://www.youtube.com/results?search_query=" + string

browser = webdriver.Chrome()
browser.get(url)

source = browser.page_source

soup = bs4.BeautifulSoup(source,'html.parser')

hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")
youtubeLinks=[]
for a in hrefs:
    youtubeLinks.append("https://www.youtube.com/"+a['href'])
    print (youtubeLinks[i])
print("End for Search，Prepare to Download and Trans")
id=0
for url in youtubeLinks:
    TransURLToMp3(url,id)
    id+=1
print("Finished Download ，Excute MoveFile")
MoveFileToFolder()