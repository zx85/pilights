from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import RPi.GPIO as GPIO
# Do setup in case it's needed


app = Flask(__name__)
app.config['SECRET_KEY'] = 'INSERT_KEY_HERE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lights.db'
db = SQLAlchemy(app)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)


class Lights(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	configName = db.Column(db.String(20), unique=True, nullable=False)
	configRed = db.Column(db.Integer)
	configGreen = db.Column(db.Integer)
	configBlue = db.Column(db.Integer)

	def __repr__(self):
	    return "Lights('"+self.configName+"', "+str(self.configRed)+", "+str(self.configGreen)+", "+str(self.configBlue)+")"

# lightsPower
# lightsColour
# presetOne ... presetEight
# config_name,config_red, config_blue, config_green

from pilights import routes


