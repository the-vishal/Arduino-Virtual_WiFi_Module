import serial
from tkinter import*
yo = Tk()
yo.wm_title("Arduino GUI")
yo.config(background='#708090',height=500,width=600)

def call():
    print ("LED is ON now")
    arduino.write(b'1')

def call2():
     print("LED is Switched OFF")
     arduino.write(b'0')

def call3():
    print("LED in blink mode")
    arduino.write(b'2')

def fade():
    arduino.write(b'3')
    print("LED in Fade MODE Brightness = ",b4.get(),"units")
    arduino.write(b'b4.get()')

khidki= Frame(yo,width=400,height=300)
khidki.grid(row=0,column=0,padx=10,pady=2)
b=Button(khidki,text="LED ON",bg='Yellow',bd=10,activebackground='#ffe4e1',command=call)


k2 =Frame(yo, width =400,height=300)
k2.grid(row=1,column=0,padx=10,pady=2)
b2 =Button(k2,bd=10,bg='red',activebackground='#ffffff',command=call2,text="LED OFF")

k3=Frame(yo,height=300,width=400)
k3.grid(row=2,column=0,padx=10,pady=2)
b3=Button(k3,text="Blink MODE",bd=10,bg='green',activebackground='#00ffff',command=call3)


k4=Frame(yo,height=300,width=300)
k4.grid(row=3,column=0,padx=10,pady=2)
b4=Scale(k4,from_=0,to=255,tickinterval=15,length=400,orient=HORIZONTAL)
w=Button(k4,text="Fade Value",command=fade,bg='Pink',activebackground='#b0e0e6')

b.pack()
b2.pack()
b3.pack()
b4.pack()
w.pack()
arduino=serial.Serial('COM3',9600)
yo.mainloop()
