from flask import Flask, render_template
from flask_basicauth import BasicAuth
import datetime
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'bill'
app.config['BASIC_AUTH_PASSWORD'] = 'chicken'

basic_auth = BasicAuth(app)

@app.route("/")
@basic_auth.required
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO BILL!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='localhost', port=3000, debug=True)
