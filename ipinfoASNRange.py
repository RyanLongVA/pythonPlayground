import sys, requests, pdb, re
from bs4 import BeautifulSoup
from subprocess import call

def start():
    page = requests.get("https://ipinfo.io/AS10310")
    asns = []
    soup = BeautifulSoup(page.content, 'lxml')
    for a in soup.find('tbody', {'class':'t-14'}):
        if a == '\n':
            continue
        asns.append(a.select('a')[0].text.strip())
    print(asns)

start()
    
