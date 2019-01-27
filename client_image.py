# Import socket module 
import socket
import os
import io
import sys
from PIL import Image
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 8888                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
print(s.recv(1024).decode("utf-8"))

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "imgs/mountain.jpeg"
abs_file_path = os.path.join(script_dir, rel_path)

image = Image.open(abs_file_path)
bytes = image.tobytes()

width, height = image.size
num_bytes = sys.getsizeof(bytes)
print("width of image =", width)
print("height of image =", height)
print("bytes in image =", sys.getsizeof(bytes))

s.sendall((str(width).encode()))
response = (s.recv(32).decode("utf-8"))

s.sendall((str(height).encode()))
response = (s.recv(32).decode("utf-8"))

s.sendall((str(num_bytes).encode()))
response = (s.recv(32).decode("utf-8"))

print(response)

if response == 'GOT SIZE':
    
    print("size of data = ", sys.getsizeof(bytes))
    '''
    while 1:
        image = open(abs_file_path, "rb")
        data = image.read(1024)
        if not data:
            break
        s.send(data)
    '''

#print(s.recv(1024).decode("utf-8"))

# close the connection 
s.close()  