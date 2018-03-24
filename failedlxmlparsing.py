import sys, requests, pdb
from lxml import html
from lxml import etree

page = requests.get("https://www.ultratools.com/tools/asnInfoResult?domainName=%s"%(sys.argv[1]))
content = html.fromstring(page.content)
tree = content.xpath("/html/body/div[3]/div/div[3]/div/div[3]")
#tree = html.fromstring(page.content)
tree2 = content.cssselect("div.tools-results-container")
for element in tree2.getiterator():
    pdb.set_trace()
    if element.get('class') == "tools-results-heading":
        print html.tostring(element)
        pdb.set_trace()
#    ASNs.append(element.text)
ASNs = []

