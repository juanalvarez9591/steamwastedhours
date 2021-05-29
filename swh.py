from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")

print("Welcome to the Steam Wasted Hours Calculator!")
print("Insert your Custom URL name!")
print("And make sure your privacy settings are public!")


insta = input("> ")
url = "https://steamcommunity.com/id/"+insta+"/games/?tab=all"
driver = webdriver.Chrome("chromedriverlocation", options=chrome_options)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")

data = soup.find_all("h5", class_ = "ellipsis hours_played")

hrsplayed = []
for i in data:
    if "h registradas" in i.text:
        hrsplayed.append(i.text.replace("h registradas","").replace(",",""))
    else: pass

totalhrsplayed = 0

for i in hrsplayed:
    totalhrsplayed += float(i)

totalhrsplayed = round(totalhrsplayed, 1)

print("You have wasted a total of "+str(totalhrsplayed)+" hours between all your games. Great work!")