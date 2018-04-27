import sys, requests, pdb, re
from bs4 import BeautifulSoup
from subprocess import call
def start():
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
    return asns

def sortASNs(asns):
    sortedASNs = []
    for a in filter(None, asns.split('\n')):
        value = int(a.split(' : ')[0].split('AS')[1])
        clength = len(sortedASNs)
        for idx, b in enumerate(sortedASNs):
            sortedv = int(b.split(' : ')[0].split('AS')[1])
            #if value > int(a.split(' : ')[0].split('AS')[1]):a
            #   it's just bigger
            if value < sortedv:
                # the value becomes smaller
                sortedASNs.insert(idx,a)
                break
            elif clength-1 == idx:
                sortedASNs.append(a)
                break
        if clength == 0:
            sortedASNs.append(a)
    return sortedASNs

def printRanges(asns):
    ipRange = []
    for a in asns.splitlines():
        casn = a.split(' : ')[0]
        cpage = requests.get('https://ipinfo.io/%s'%(casn)).text
        soup = BeautifulSoup(cpage, 'lxml')
        dataContainer = soup.find('tbody', {'class':'t-14'})
        if dataContainer == None:
            continue
        for b in dataContainer:
            if b == '\n':
                continue
            ipRange.append(b.select('a')[0].text.strip())
    print ' , '.join(ipRange)

def main():
    a = '\n'.join(sortASNs(start()))
    printRanges(a)

if __name__== "__main__":
    main()

