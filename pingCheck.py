import socket, pdb

domainsList = open('tempdnsrecon.txt', 'r')
successful = []
fails = []
for a in domainsList.readlines(): 
            if 'PTR' not in a:
                continue
            try: 
                chost = a.split()[2]
                b = socket.gethostbyname(chost)
            except Exception,e:
                if e[0] == -2:
                    fails.append(chost)
                    print 'Failed: '+chost
                    continue
                else:
                    print e
                    exit()
            if b == '192.168.0.1':
                print 'Failed (locally?): '+chost
                fails.append(chost)
                continue
            else:
                successful.append(chost)
                pass
pdb.set_trace()
