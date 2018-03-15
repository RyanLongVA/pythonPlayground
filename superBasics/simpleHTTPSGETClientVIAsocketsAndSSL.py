import socket, ssl, sys, time

def recv_timeout(the_socket, timeout=2):
    the_socket.setblocking(0)
    total_data = []
    data = ''
    begin=time.time()
    while 1:
        if total_data and time.time()-begin > timeout:
            break
        elif time.time()-begin > timeout*2:
            break
        try: 
            data = the_socket.recv(8192)
            if data: 
                print data
                total_data.append(data)
                begin = time.time()
            else: 
                time.sleep(0.1)
        except:
            pass

#There's the obvious argparse, which would be overkill for the simple script
if len(sys.argv) != 3:
    print "usage: python script.py {url} {port}"
    exit()

arg_url = sys.argv[1]
arg_port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
try: 
    conn.connect((arg_url, arg_port))
    conn.write("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%arg_url)
    recv_timeout(conn)
    conn.close()
except Exception,e:
    print e
    pass

