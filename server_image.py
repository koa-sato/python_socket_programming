# first of all import the socket library 
import socket                
import os
import sys
from PIL import Image

# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 8888 but it can be anything 
port = 8888                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print("socket binded to %s" %(port))
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
    # Establish connection with client. 
    c, addr = s.accept()      
    print('Got connection from', addr)
    
    # send a thank you message to the client.  
    c.send ('Thank you for connecting'.encode())

    data = c.recv(32)
    width = data.decode()
    print ("Client says width of image = " + width)
    c.send("GOT WIDTH".encode())


    data = c.recv(32)
    height = data.decode()
    print ("Client says height of image = " + height)
    c.send("GOT HEIGHT".encode())


    data = c.recv(1024)
    num_bytes = data.decode()
    print ("Client says size of image = " + num_bytes)
    c.send("GOT SIZE".encode())


    #data = c.recv(int(num_bytes))
    '''
    res = bytearray()
    while 1:
        t = c.recv(1024)
        if not t:
            break
        res += t
    g = open("Client.jpg", "wb")
    g.write(res)
    g.close()

    print("Image received and recreated")
    print("size of data = ", sys.getsizeof(data))

    image = Image.frombytes('RGBA', (int(width),int(height)), data, 'raw')

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "savedImgs/mountain.jpeg"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, 'wb')
    f.write(image)
    f.close()
    '''
  
    # Close the connection with the client 
    c.close() 