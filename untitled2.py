import socket
import threading
import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass

ACCESS_list=['oz7XKmC5C4GuiNr8waE8','1p1mKEY3xW32E9COUyqD']                #Token of your device
broker="demo.thingsboard.io"   			    #host name
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = 11228
ports=1883

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening on port", str(port))

def thr(c,addr,n):
     
    global info
    while True:
        sentence = c.recv(1024).decode()
        
        payload="{"
        payload+="\"Temperature"+str(n)+"\":"+str(sentence)+",";
        sentence = c.recv(1024).decode()
        payload+="\"Humidity"+str(n)+"\":"+str(sentence); 
        payload+="}"
        ret= clients[n-1].publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
        print("Please check LATEST TELEMETRY field of your device")
        print(str(payload)+"from device with IP"+str(addr));
        
        
        


info=[] 
n=0 
clients=[]
while True: 
    c, addr = s.accept()
    n+=1
    info.append(addr)
    print('current number of clients', str(n))
    print('clients info', info)
    client= paho.Client("control1")   
    clients.append(client)                 #create client object
    client.on_publish = on_publish  
    ACCESS_TOKEN=ACCESS_list[n-1]                   #assign function to callback
    client.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
    client.connect(broker,ports,keepalive=60)           #establish connection
    thread=threading.Thread(target=thr, args=(c, addr,n))
    thread.start()
"""
c, addr = s.accept()
n+=1
info.append(addr)
print('current number of clients', str(n))
print('clients info', info)
ACCESS=ACCESS_list[1]
client2= paho.Client("control1")
clients.append(client2)                    #create client object
client2.on_publish = on_publish                     #assign function to callback
client2.username_pw_set(ACCESS)               #access token from thingsboard device
client2.connect(broker,ports,keepalive=60)           #establish connection
thread=threading.Thread(target=thr, args=(c, addr,n))
thread.start()
"""