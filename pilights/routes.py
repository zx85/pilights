from flask import render_template, url_for, flash, redirect, request
from pilights import app,Lights,db,functions
import RPi.GPIO as GPIO
# Do setup in case it's needed
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
# Start with the screen off because otherwise it stays on after reboot
GPIO.output(18,GPIO.LOW)

#dictionary for presets
presetSwitcher = {
    1: "presetOne",
    2: "presetTwo",
    3: "presetThree",
    4: "presetFour",
    5: "presetFive",
    6: "presetSix",
    7: "presetSeven",
    8: "presetEight",
    }

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/local")
def local():
    return render_template('local.html')

@app.route("/getdb")
def getDB():
    param = request.args.get('param', '')
    lightsDB=Lights.query.filter_by(configName=param).first()
    return str(lightsDB.configRed)+","+str(lightsDB.configGreen)+","+str(lightsDB.configBlue)

@app.route("/getpresets")
def getPresets():
    thesePresets=Lights.query.filter(Lights.configName.like("preset%")).all()
    presetOutput=""
    for eachPreset in thesePresets: 
        presetOutput=presetOutput+eachPreset.configName+","+str(eachPreset.configRed)+","+str(eachPreset.configGreen)+","+str(eachPreset.configBlue)+"|"
        ##
    return presetOutput
        

@app.route("/setdb")
def setDB():
    param = request.args.get('param', '')
    paramRed = request.args.get('red', 9000)
    paramGreen = request.args.get('green', 9000)
    paramBlue = request.args.get('blue', 9000)
    lightsDB=Lights.query.filter_by(configName=param).first()
    if paramRed !=9000: lightsDB.configRed=paramRed
    if paramGreen !=9000: lightsDB.configGreen=paramGreen
    if paramBlue !=9000: lightsDB.configBlue=paramBlue
    db.session.commit()
    lightsDB=Lights.query.filter_by(configName=param).first()
    return str(lightsDB.configRed)+","+str(lightsDB.configGreen)+","+str(lightsDB.configBlue)


@app.route("/setlights")
def setLights():
    paramPreset = request.args.get('preset',0)
    paramRed = request.args.get('red', False)
    paramGreen = request.args.get('green', False)
    paramBlue = request.args.get('blue', False)
    paramDb = request.args.get('db', False)
    paramDec = request.args.get('dec', False)
    lightsDB=Lights.query.filter_by(configName="lightsColour").first()

    # this bit for presets overriding the RGB
    if paramPreset != 0:
        paramDb=True
    # some furkling required to get presets to number
        param=presetSwitcher.get(int(paramPreset),"presetOne")
        lightsPresetDB=Lights.query.filter_by(configName=param).first()
        paramRed=lightsPresetDB.configRed
        paramGreen=lightsPresetDB.configGreen
        paramBlue=lightsPresetDB.configBlue

    # running the separate function to be kinder to animals (low power suppply)
    doLEDs(paramRed,paramGreen,paramBlue,paramDec)
    
    if paramDb:
        if paramRed:
            lightsDB.configRed=paramRed
        if paramGreen:
            lightsDB.configGreen=paramGreen
        if paramBlue:
            lightsDB.configBlue=paramBlue
        db.session.commit()
    return 'setlights R:'+str(int(paramRed))+ ' G:'+str(int(paramGreen))+' B:'+str(int(paramBlue))

@app.route("/lightspower")
def lightsPower():
    param=request.args.get('param',0)
    if (param=="true" or param=="on"):
        truth="It is true"
        thisLightsColour=Lights.query.filter_by(configName="lightsColour").first()
        thisLightsPower=Lights.query.filter_by(configName="lightsPower").first()
        thisLightsPower.configRed=thisLightsColour.configRed
        thisLightsPower.configGreen=thisLightsColour.configGreen
        thisLightsPower.configBlue=thisLightsColour.configBlue
        thisLightsPower=Lights.query.filter_by(configName="lightsPower").first()
        db.session.commit()
    else:
        truth="It is false"
        thisLightsPower=Lights.query.filter_by(configName="lightsPower").first()
        thisLightsPower.configRed=0
        thisLightsPower.configGreen=0
        thisLightsPower.configBlue=0
        db.session.commit()
        thisLightsPower=Lights.query.filter_by(configName="lightsPower").first()
    truth=str(thisLightsPower.configRed)+","+str(thisLightsPower.configGreen)+","+str(thisLightsPower.configBlue)
    
    doLEDs(thisLightsPower.configRed,thisLightsPower.configGreen,thisLightsPower.configBlue)
    return 'lights: '+truth

@app.route("/screenoff")
def screenOff():
    GPIO.output(18,GPIO.LOW)
    return 'screenoff'

@app.route("/screenon")
def screenOn():
    GPIO.output(18,GPIO.HIGH)
    return 'screenon'

@app.route("/debug")
def debugMessage():
    return 'debug'


