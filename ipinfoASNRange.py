import sys, requests, pdb, re
from bs4 import BeautifulSoup
from subprocess import call

def start():
    # Variable sytax: AS{integer}
    page = requests.get("https://ipinfo.io/%s"%(sys.argv[1]))
    asns = []
    soup = BeautifulSoup(page.content, 'lxml')
    for a in soup.find('tbody', {'class':'t-14'}):
        if a == '\n':
            continue
        asns.append(a.select('a')[0].text.strip())
    for a in asns: 
        print a

start()
    
