import socket
import serial



s = socket.socket()         # Create a socket object
host = '192.168.43.173'    #your ip address
port = 5555
s.bind((host, port))

arduino = serial.Serial('COM3', 9600) #replace COM3 with your arduino connected port


s.listen(5)
c, addr = s.accept()
while True:
   c, addr = s.accept()
   url = c.recv(1024)
   command = (str(url)[-2])
   #print(command)

   if command == '0':
       arduino.write(b'0')

   elif command == '1':
       arduino.write(b'1')

