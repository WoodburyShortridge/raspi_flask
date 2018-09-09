from flask import Flask, render_template, redirect
from flask_basicauth import BasicAuth
import datetime
import env

# gate code imports

import time
import RPi.GPIO as GPIO

# set GPIO mode
GPIO.setmode(GPIO.BCM)

def openGate():
   GPIO.setup(17,GPIO.OUT)
   GPIO.output(17,GPIO.LOW)
   time.sleep(1.45)
   GPIO.output(17,GPIO.HIGH)

def closeGate():
   GPIO.setup(17,GPIO.OUT)
   GPIO.output(17,GPIO.LOW)
   
   GPIO.setup(27,GPIO.OUT)
   GPIO.output(27,GPIO.LOW)

   time.sleep(1.45)

   GPIO.output(17,GPIO.HIGH)

   GPIO.output(27,GPIO.HIGH)
   

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = env.config["auth"]["name"]
app.config['BASIC_AUTH_PASSWORD'] = env.config["auth"]["password"]

basic_auth = BasicAuth(app)

gate = 0
message = "The coop is shut!"

@app.route("/")
@basic_auth.required
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO BILL!',
      'time': timeString,
      'gate' : gate,
      'message' : message
      }
   return render_template('main.html', **templateData)

@app.route("/gate/<int:gate_action>")
@basic_auth.required
def action(gate_action):

   global gate, message

   if gate_action == 1:
      print (action, "open the gate")
      # Gate open code here
      openGate()
      message = "The coop is open!"
      gate = 1

   elif gate_action == 0:
      print (action, "close the gate")
      # Gate close code here
      closeGate()
      message = "The coop is shut!"
      gate = 0

   else:
      print ("hacker alert!")
      message = "You can't do that!"

   return redirect('/')


if __name__ == "__main__":
   app.run(host=env.config["ip"], port=3000, debug=True)
   GPIO.cleanup()
