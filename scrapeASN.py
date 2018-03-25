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

def callASNsOnBGP(asns):
    for line in asns.split('\n'):
        print line
        cprompt = raw_input('Enter to continue')
        try:
            call('chromium https://bgp.he.net/%s#_prefixes'%(line.split(' : ')[0]), shell=True)
        except Exception, e:
            print e
            exit()

def main():
    a = sortASNs(start())
    print a.join('\n')

if __name__== "__main__":
    main()

#page.select('.tool-results-container')
