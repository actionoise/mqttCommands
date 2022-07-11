from RpiMotorLib import RpiMotorLib
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
GPIO.setmode(GPIO.BCM)

nord=[21,20,16,12]
sud=[12,16,20,21]
mymotor=RpiMotorLib.BYJMotor('MyMotorOne','28BYJ')  #Stepper Motor
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)   #GPIO Pins connected to driver L298n
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)   
GPIO.setup(22,GPIO.OUT)   #GPIO Pins connected to driver L298n
GPIO.setup(23,GPIO.OUT)   #GPIO connected to driver L298n
GPIO.setup(24,GPIO.OUT)   #GPIO connected to driver L298n
GPIO.setup(5,GPIO.OUT)    #GPIO connected to driver L298n
GPIO.output(17,GPIO.HIGH) #relay connected with a bc337 transistor for deactivate the motor driver during the boot
a=GPIO.PWM(22,100)
b=GPIO.PWM(23,100)
c=GPIO.PWM(24,100)
d=GPIO.PWM(5,100)
#stepper motors

def on_connect(client, userdata, flags, rc):
       print(f"connected with result code {rc}")
       client.subscribe("Pu here your subcription code") #topic
mymessage =" "

def on_message(client,userdata,msg):
    global mymessage
    mymessage = str (f"{msg.payload}")
    print (mymessage)
    if(mymessage== "b'nord'"):
        print('comando ricevuto')
        mymotor.motor_run(sud, .1/50,30,False,False,'half', .100)
    
    if(mymessage=="b'sud'"):
            print('comando ricevuto')
            mymotor.motor_run(nord, .1/50,30,False,False,'half', .100)
            
 
    
  
    if(mymessage=="b'right'"):
                    print("right")
                    GPIO.output(22,GPIO.LOW)  #right
                    GPIO.output(23,GPIO.HIGH)
                    GPIO.output(24,GPIO.HIGH)
                    GPIO.output(5,GPIO.LOW)
                   
                   
                    
    if(mymessage=="b'stop'"):
                    print("stop")
                    GPIO.output(22,GPIO.LOW)  #stop
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.LOW)                          
                    
 
     
    if(mymessage=="b'left'"):
            print("left")
            GPIO.output(22,GPIO.HIGH)  #left
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(5,GPIO.HIGH)
           
            


    if(mymessage=="b'bottom'"):
            print("bottom")
            GPIO.output(22,GPIO.HIGH)  #bottom
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(5,GPIO.LOW)
            
            


    if(mymessage=="b'gora'"):
            print("GoRallent")
            GPIO.output(22,GPIO.LOW)  #Gorallent
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(5,GPIO.HIGH)
            


    if(mymessage=="b'go'"):
        print("go no obstacle")
        GPIO.output(22,GPIO.LOW)  #go straight.
        GPIO.output(23,GPIO.HIGH)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
            
            
            
           


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.will_set("raspberry/status",b'{"status":"off"}')
client.connect("broker.emqx.io",1883,60)



client.loop_forever()
    



        
