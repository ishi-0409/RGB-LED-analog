import RPi.GPIO as GPIO
import ADC0834
GPIO.setmode(GPIO.BCM)
from time import sleep

RED=23
GREEN=24
BLUE=21

GREENbutton=6
YELLOWbutton=5

GPIO.setup(GREENbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(YELLOWbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

REDpwm=GPIO.PWM(RED,1000)
GREENpwm=GPIO.PWM(GREEN,1000)
BLUEpwm=GPIO.PWM(BLUE,1000)

REDpwm.start(0)
GREENpwm.start(0)
BLUEpwm.start(0)

ADC0834.setup()
index=[0,0,0]

try:
    while True:
        REDanalog=ADC0834.getResult(0)
        GREENanalog=ADC0834.getResult(1)
        BLUEanalog=ADC0834.getResult(2)
        print('red=',REDanalog,'green=',GREENanalog,'blue=',BLUEanalog)
        REDDC=REDanalog*100/255
        GREENDC=GREENanalog*100/255
        BLUEDC=BLUEanalog*100/255
        REDpwm.ChangeDutyCycle(REDDC)
        GREENpwm.ChangeDutyCycle(GREENDC)
        BLUEpwm.ChangeDutyCycle(BLUEDC)
        if GPIO.input(GREENbutton)==GPIO.LOW:
            index=[REDDC,GREENDC,BLUEDC]
            print('save the color',index)
            sleep(0.3)
        if GPIO.input(YELLOWbutton)==GPIO.LOW:
            REDpwm.ChangeDutyCycle(index[0])
            GREENpwm.ChangeDutyCycle(index[1])
            BLUEpwm.ChangeDutyCycle(index[2])
            print('Update')
            sleep(0.3)
        sleep(0.3)
except KeyboardInterrupt:
    REDpwm.stop()
    GREENpwm.stop()
    BLUEpwm.stop()
    GPIO.cleanup()





    