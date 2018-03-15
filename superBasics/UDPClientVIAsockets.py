import socket, sys, time

#There's the obvious argparse, which would be overkill for the simple script
if len(sys.argv) != 3:
    print "usage: python script.py {url} {port}"
    exit()

arg_url = sys.argv[1]
arg_port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("ASDFASDF",(arg_url,arg_port))
data, addr = s.recvfrom(4096)

print data
# print recv_timeout(s)
# s.close()



