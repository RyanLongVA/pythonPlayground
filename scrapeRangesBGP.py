import requests, sys, pdb, re
from bs4 import BeautifulSoup 

#Combine with scrapeASN.py and make output in 2 versions... one that's easy to paste into a document and keep notes on and the second as just ranges (The idea eventually use the scope to get the hce)

#def getIpsFromASN(ASN):
#    page = requests.get("https://bgp.he.net/%s#_prefixes"%(ASN))
#    soup = BeautifulSoup(page.content)
#    for a in soup.find('div', 


prefixes = []

page = requests.get("https://bgp.he.net/AS24572#_prefixes")
print page.content
pdb.set_trace()

