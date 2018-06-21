from flask import Flask, render_template
from flask_basicauth import BasicAuth
import datetime
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'bill'
app.config['BASIC_AUTH_PASSWORD'] = 'chicken'

basic_auth = BasicAuth(app)

gate = "down"

@app.route("/")
@basic_auth.required
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO BILL!',
      'time': timeString,
      'gate' : gate
      }
   return render_template('main.html', **templateData)

@app.route("/gate/<action>")
@basic_auth.required
def action(action):

   global gate

   if action == "up":
      print (action, "Let the chickens loose!")
      message = "Chickens are loose!"
      gate = "up"

   elif action == "down":
      print (action, "close the hatch")
      message = "The coop is shut!"
      gate = "down"

   else:
      print ("hacker alert!")
      message = "You can't do that!"

   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")

   templateData = {
      'title' : message,
      'time': timeString,
      'gate' : gate
   }

   return render_template('main.html', **templateData)


if __name__ == "__main__":
   app.run(host='localhost', port=3000, debug=True)
