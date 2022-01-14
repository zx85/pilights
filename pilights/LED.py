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
        Red=lightsDB.configRed
        Green=lightsDB.configGreen
        Blue=lightsDB.configBlue
    if endDec:
       multiplier=2.575757
    else:
       multiplier=1

    if endRed and (endRed!=Red):
        endRed=(int(endRed)*multiplier)%256
        Red=int(Red)
        if endRed>Red:
            intRed=eachJump
        else:
           intRed=eachJump*-1
    else:
        endRed=Red
        intRed=0
    if endGreen and (endGreen!=Green):
        endGreen=(int(endGreen)*multiplier)%256
        Green=int(Green)
        if endGreen>Green:
            intGreen=eachJump
        else:
           intGreen=eachJump*-1
    else:
        endGreen=Green
        intGreen=0
    if endBlue and (endBlue!=Blue):
        endBlue=(int(endBlue)*multiplier)%256
        Blue=int(Blue)
        if endBlue>Blue:
            intBlue=eachJump
        else:
           intBlue=eachJump*-1
    else:
        endBlue=Blue
        intBlue=0

    print("endRed: "+str(endRed)+" | endGreen: "+str(endGreen)+" | endBlue: "+str(endBlue))
    print("Red: "+str(Red)+" | Green: "+str(Green)+" | Blue: "+str(Blue))
    # time to loop the loop
    print("Looping the loop")
    while (endRed!=Red) and (endGreen!=Green) and (endBlue!=Blue):
        print("endRed: "+str(endRed)+" | endGreen: "+str(endGreen)+" | endBlue: "+str(endBlue))
        print("Red: "+str(Red)+" | Green: "+str(Green)+" | Blue: "+str(Blue))
        if Red!=endRed:
            Red=Red+intRed
        if Green!=endGreen:
            Green=Green+intGreen
        if Blue!=endBlue:
            Blue=Blue+intBlue
        print("endRed: "+str(endRed)+" | endGreen: "+str(endGreen)+" | endBlue: "+str(endBlue))
        print("Red: "+str(Red)+" | Green: "+str(Green)+" | Blue: "+str(Blue))
        pi.set_PWM_dutycycle(19,Green)
        pi.set_PWM_dutycycle(20,Red)
        pi.set_PWM_dutycycle(21,Blue)
        time.sleep(eachSleep)
