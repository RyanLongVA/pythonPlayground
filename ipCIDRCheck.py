import sys

#input checks

if len(sys.argv) < 3:
    print 'python script.py 127.0.0.1 127.0.0.1/32'
    exit()

#Directly from stackoverflow

def ipToInt(ip):
    o = map(int, ip.split('.'))
    res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
    return res

def isIpInSubnet(ip, ipNetwork, maskLength):
    ipInt = ipToInt(ip)#my test ip, in int form

    maskLengthFromRight = 32 - int(maskLength)

    ipNetworkInt = ipToInt(ipNetwork) #convert the ip network into integer form
    binString = "{0:b}".format(ipNetworkInt) #convert that into into binary (string format)

    chopAmount = 0 #find out how much of that int I need to cut off
    for i in range(maskLengthFromRight):
        if i < len(binString):
            chopAmount += int(binString[len(binString)-1-i]) * 2**i

    minVal = ipNetworkInt-chopAmount
    maxVal = minVal+2**maskLengthFromRight -1

    return minVal <= ipInt and ipInt <= maxVal

def main():
    print isIpInSubnet(sys.argv[1],sys.argv[2].split('/')[0],sys.argv[2].split('/')[1])

if __name__ == '__main__':
    main()
