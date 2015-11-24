#UDPPingClient.py
from __future__ import division
import time
import sys
from socket import *

#initialize some variables
myMax = 0
myMin = 1
mySum = 0
myNum = int(sys.argv[3])
numLost = 0

#Sends N number of datagrams
for pings in range(myNum):
    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set 1 second timeout value
    clientSocket.settimeout(1)

    #Ping to server
    message = 'wooooooooo'
    
    #Server address
    addr = ('127.0.0.1', 12000)

    #Send ping and track send time
    start = time.time()
    clientSocket.sendto(message, addr)

    #If data is received back from server, print 
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        now = time.strftime("%c")
        rtt = end - start
        
        #determine RTT
        if rtt > myMax:
            myMax = rtt
        if rtt < myMin:
            myMin = rtt
        mySum = mySum + rtt
        
        #Print stuff
        print 'Reply from %s: Ping %d %s' %(str(addr), pings+1, now)
        print 'RTT: %f' %(rtt)    

    #If data is not received back from server, print it has timed out and track number of packets lost
    except timeout:
        print 'Request timed out'
        numLost = numLost + 1

#Some math and printing for after all packets have been sent
myAvg = mySum / myNum
myLoss = (numLost / myNum) * 100
lossMsg = str(myLoss) + '%'
print 'Max = %f  Min = %f  Average = %f  Packet Loss = %s' %(myMax, myMin, myAvg, lossMsg)