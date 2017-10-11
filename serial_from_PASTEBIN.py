#Beautifulsoup,serial-arduino data pickup from webhost here PASTEBIN
import bs4 as bs
import urllib.request
import serial
import time

def Monitor_PasteBIN():
 sauce = urllib.request.urlopen('https://pastebin.com/raw/MuS8ZYiX').read()
 soup = bs.BeautifulSoup(sauce, "html.parser")
 print(soup.text)
 global inp
 inp=soup.text

arduino=serial.Serial('COM3',9600)
#LED operation

while True:
 Monitor_PasteBIN()
 if(inp=='0' or inp=='OFF'):
    print("OFF State")
    arduino.write(b'0')

 if(inp=='1' or inp=='ON'):
    print("ON State")
    arduino.write(b'1')

# ------------------------------------- Completed to requirement --------------------------------------------