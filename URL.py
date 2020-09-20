import bs4 
from selenium import webdriver 

string = "pop+beat";

url = "https://www.youtube.com/results?search_query=" + string

browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
browser.get(url)

source = browser.page_source

soup = bs4.BeautifulSoup(source,'html.parser')

hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")
for a in hrefs:
    print (a['href'])


