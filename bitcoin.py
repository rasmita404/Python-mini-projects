#from __pycache__ import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import ssl

URL = "https://www.google.com/search?q="
Query = "bitcoin+price+in+usd"

def scrape():
    r = requests.get(URL+Query)
    s = BeautifulSoup(r.text, 'html.parser')
    ans = s.find("div", class_ = "BNeawe iBp4i AP7Wnd")
    return ans.text

price = scrape()
print(price)
#not working
