from ast import Break
from ctypes import sizeof
import cv2 as cv
import numpy as np
from Take_Photo import TakePhoto
from contours import ImageProcessing
from Scaling import Scaling
import keyboard
import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.12.90"                                             # The host machine is (192.168.12.90") or you can use localhost IP 127.0.0.1 for testing
port = 2222

msg_recv=""
client.connect((host,port))                      # Connecting client(PC) to the server 
msg_recv=client.recv(1024)                       # Reciving msg from Robot(Server)


j=0                                               # Initial values
n=0                                               # Initial values

while True:
    
    
    if keyboard.is_pressed("q"):                                     # Press q to break out of the loop
        print("q")
        break
    elif j == n  and msg_recv.decode() != "Busy":                    # If there is no object or robot is done with preveus task Take new Photo
        print("Taking New Photo ")
        Image = TakePhoto()                                          # Functinion take new Photo and save it on Image and on file /Photos
        Object,Image2=ImageProcessing()                              # NB! Fuction uses image that is saved on file Photos and give s out two outputs Objects detected and Image2 that contains Objects detected
        Data=Scaling(Object)                                         # Function takes inn Objects tha are detected and gives out name and coordinate of the object 
        n=len(Data)                                                  # Numbers of detected objects
        print("Object detected ",n)                                  # Number of Object detected + GoHome if there was object detected NB! GoHome is not object is just instruction to Rapid code so n-1 if you whish to ext nr of object
        j=0                                                          # Reset J for while loop
        cv.namedWindow("Work Place",cv.WINDOW_NORMAL)                # Creat window to show Image and name it Work Place
        cv.resizeWindow("Work Place",int(1920*0.9), int(1080*0.9))   # Resize the window to it OG size and reduse by 10%  just to see all the workplace
        cv.imshow("Work Place", Image2)                              # Show the image
        cv.waitKey(1000)                                             # Show the image for 1 second                     
        cv.destroyAllWindows()                                       # closew the window
    
    while j != n:                                      #  This while loop runs when there is object detected                                   
       
        if msg_recv.decode() == "Ready":               # Check if Robot is ready to receive Data
            client.send(bytes(Data[j],"utf-8"))        # Send object on the list one by one
            j=j+1                                      # counting object that are send 
        elif keyboard.is_pressed("q"):
            print("Stopp")
            Break 
        else:
            j=j
        msg_recv=client.recv(1024)                    # Receiving msg from Robot on his state Ready or Busy 
        print(msg_recv.decode(),"  "," Job done", " ",j," Out of ",n )       
        if j==n and msg_recv.decode() == "Busy":
          #client.send(bytes("GoHome 0 0","utf-8"))
          print("GO Home")
        
             
# Waiting is done on the frist loop 
    if msg_recv.decode() == "Busy":                   # Waiting for msg Ready form Robot since it is busy
        print("Waiting for msg")
        msg_recv=client.recv(1024)                     # Waiting for msg  That mean waiting for robot to be ready
        print("I have  ",msg_recv.decode())
            
   

client.close()


    