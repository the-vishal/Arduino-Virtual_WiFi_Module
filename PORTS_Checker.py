#Lists all active serial ports and devices connected to them
import serial.tools.list_ports

ports= list(serial.tools.list_ports.comports())
for p in ports:
    print(p)
 # ------------------------------------- Completed to requirement --------------------------------------------