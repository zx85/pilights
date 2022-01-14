import RPi.GPIO as GPIO
import pigpio

def doLEDs(paramRed,paramGreen,paramBlue,paramDec=false):
    pi=pigpio.pi()
    if paramRed !=9000:
        if paramDec == 'true':
            paramRed=int(int(paramRed)*2.575757)
        pi.set_PWM_dutycycle(20,int(paramRed)%256)
    if paramGreen !=9000:
        if paramDec == 'true':
            paramGreen=int(int(paramGreen)*2.575757)
        pi.set_PWM_dutycycle(19,int(paramGreen)%256)
    if paramBlue !=9000:
        if paramDec == 'true':
            paramBlue=int(int(paramBlue)*2.575757)
        pi.set_PWM_dutycycle(21,int(paramBlue)%256)

