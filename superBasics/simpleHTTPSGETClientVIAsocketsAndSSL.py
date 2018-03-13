import socket, ssl, sys

#There's the obvious argparse, which would be overkill for the simple script
if len(sys.argv) != 3:
    print "usage: python script.py {url} {port}"
    exit()

arg_url = sys.argv[1]
arg_port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sslContext = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
# sslContext.options |= ssl.OP_NO_TLSv1 | ssl.OP_NOTLSv1_1
conn = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
try: 
    conn.connect((arg_url, arg_port))
    conn.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%arg_url)
    print(conn.recv(4096))
    conn.close()
except:
    pass

