import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import sys


def discount(link):

    url = link
    response = requests.get(url)

    pool = BeautifulSoup(response.text, 'html.parser')

    if("trendyol" in url):
        trendyol(pool)
    #if("hepsiburada" in url):



def trendyol(pool):

    tag = pool.findAll('span',class_='prc-slg')
    for s in tag:
        if("TL" in str(s)):
            print(s.string)
            break

user_input = input("Enter link of item : ") 
discount(user_input)

