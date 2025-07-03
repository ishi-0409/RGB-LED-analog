This is the code for SunFounder Da Vinci Kit for Raspberry Pi. This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied wa rranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

davinci-kit-for-raspberry-pi comes with ABSOLUTELY NO WARRANTY; for details run ./show w. This is free software, and you are welcome to redistribute it under certain conditions; run ./show c for details.

SunFounder, Inc., hereby disclaims all copyright interest in the program 'davinci-kit-for-raspberry-pi' (which makes passes at compilers).

Mike Huang, 21 August 2015

Mike Huang, Chief Executive Officer

Modified by ishi-0409, 2025


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





    
