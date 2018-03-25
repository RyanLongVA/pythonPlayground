import sys, requests, pdb, re
from bs4 import BeautifulSoup
    
page = requests.get("https://www.ultratools.com/tools/asnInfoResult?domainName=%s"%(sys.argv[1]))

asns = ''

soup = BeautifulSoup(page.content)
for a in soup.find('div', {"class": "tool-results-container"}):
    if a == '\n':
        continue
    if (a['class'] == ['tool-results-heading']):
        asns += a.text+" : "
    if a['class'] == ['tool-results']:
        #Dig into the architecture and get only the owner
        asns += a.select("span")[7].text+'\n'
print asns
#page.select('.tool-results-container')
