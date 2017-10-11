# Recieving Mobile Light sensor data coming on PORT mentioned, from 'Sensor Node Free.apk
# Sending serial command to arduino accordingly'
import socket
import time
import bs4 as bs
import serial
import win32com.client as wincl

#IP and ports
UDP_IP = "192.168.43.173"
UDP_PORT = 5555

#AF_INET -- Addressing from internet IP
#SOCK_DGRAM -- Datagram based protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


#Arduino serial port and BaudRate
arduino =serial.Serial('COM3',9600)


#logic to collect data from PORT and check when to turn arduino LED On
def acc():
    soup = bs.BeautifulSoup(data, 'lxml')
    Intensity = int(float(soup.text))
    print(Intensity)
    if Intensity<=10:
        arduino.write(b'1')

    else:
        arduino.write(b'0')


#Recieving data from ports continously
while True:
    data, addr = sock.recvfrom(4800)
    # print(data)
    acc()
    time.sleep(0)




    # ------------------------------------- Completed to requirement --------------------------------------------
# ideas : Sensor calibration, left,right kaha pr h, if advance then making a gamepad