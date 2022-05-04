import RPi.GPIO as GPIO
import pigpio
import time

def doLEDs(lightsDB,endRed=False,endGreen=False,endBlue=False,endDec=False,fromZero=False):
    pi=pigpio.pi()

# Variables of significance
    eachJump=1
    eachSleep=0.1
# 
    if fromZero:
        Red=0
        Green=0
        Blue=0
    else:
        Red=int(lightsDB.configRed)
        Green=int(lightsDB.configGreen)
        Blue=int(lightsDB.configBlue)
    if endDec:
       multiplier=2.575757
    else:
       multiplier=1

    if endRed and (int(endRed)!=Red):
        endRed=(int(endRed)*multiplier)%256
        if endRed>Red:
            intRed=eachJump
        else:
           intRed=eachJump*-1
    else:
        endRed=Red
        intRed=0

    if endGreen and (int(endGreen)!=Green):
        endGreen=(int(endGreen)*multiplier)%256
        if endGreen>Green:
            intGreen=eachJump
        else:
           intGreen=eachJump*-1
    else:
        endGreen=Green
        intGreen=0

    if endBlue and (int(endBlue)!=Blue):
        endBlue=(int(endBlue)*multiplier)%256
        if endBlue>Blue:
            intBlue=eachJump
        else:
           intBlue=eachJump*-1
    else:
        endBlue=Blue
        intBlue=0

    # time to loop the loop
    while (endRed != Red) or (endGreen != Green) or (endBlue != Blue):
        if Red!=endRed:
            Red=Red+intRed
        if Green!=endGreen:
            Green=Green+intGreen
        if Blue!=endBlue:
            Blue=Blue+intBlue
        pi.set_PWM_dutycycle(19,Green)
        pi.set_PWM_dutycycle(20,Red)
        pi.set_PWM_dutycycle(21,Blue)
        time.sleep(eachSleep)
