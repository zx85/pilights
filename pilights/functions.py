import RPi.GPIO as GPIO
import pigpio

def doLEDs(paramRed=False,paramGreen=False,paramBlue=False,paramDec=False):
    pi=pigpio.pi()
    if paramRed:
        if paramDec:
            paramRed=int(int(paramRed)*2.575757)
        pi.set_PWM_dutycycle(20,int(paramRed)%256)
    if paramGreen:
        if paramDec:
            paramGreen=int(int(paramGreen)*2.575757)
        pi.set_PWM_dutycycle(19,int(paramGreen)%256)
    if paramBlue:
        if paramDec:
            paramBlue=int(int(paramBlue)*2.575757)
        pi.set_PWM_dutycycle(21,int(paramBlue)%256)

