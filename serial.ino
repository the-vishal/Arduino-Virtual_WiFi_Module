int led = 13;//Connect LED to pin 13 and ground.
int inp;//Input, either directly from serial monitor from user or from Python Serial library.

void setup() 
{
Serial.begin(9600);
pinMode(led,OUTPUT);
}

void loop() 
{
if(Serial.available()>0)
   {inp = Serial.read();

      if(inp == '1')// set 1 as high command to turn LED on.
       { digitalWrite(led,HIGH);
        }
      if(inp == '0')//set 0 as low command to turn LED off.
        { digitalWrite(led,LOW);
          }
          
    }
}
