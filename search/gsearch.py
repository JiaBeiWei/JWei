
from googlesearch import search 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

import webbrowser  

query = input("What's up > ")

for j in search(query, tld="co.in", num=10, stop=2, pause=2): 
  print("OPENING",j) 
  webbrowser.open_new_tab(j)

