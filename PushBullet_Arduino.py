#LDR,Arduino light jaane pr pushbullet ---> led on krni h ya nhi
from pushbullet import PushBullet
from urllib3 import  request
import requests
import serial

api_key = 'YourPushBulletAPIKeyHere'
pb = PushBullet(api_key)
push = pb.push_note("Arduino","Bhai Light Chali gyi..LED ON kru?")

#print(pushes)

def check_val():

 global val
 pushes = pb.get_pushes()
 val = pushes[0]['body']
 #print(val)

arduino = serial.Serial('COM3',9600)

while True:
 check_val()
 if(val =='1' or val=='ON' or val=='ha'):
    arduino.write(b'1')

 if(val=='0'or val=='nhi' or val=='OFF'):
    arduino.write(b'0')

 # ------------------------------------- Completed to requirement --------------------------------------------