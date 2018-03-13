import socket, sys, time


def recv_timeout(the_socket,timeout=2):
    #make socket non blocking
    the_socket.setblocking(0)
     
    #total data partwise in an array
    total_data=[];
    data='';
     
    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break
         
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
         
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                print data
                #change the beginning time for measurement
                begin = time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
     
    #join all parts to make final string
    return ''

#There's the obvious argparse, which would be overkill for the simple script
if len(sys.argv) != 3:
    print "usage: python script.py {url} {port}"
    exit()

arg_url = sys.argv[1]
arg_port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((arg_url, arg_port))
s.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%arg_url)
print recv_timeout(s)
s.close()



