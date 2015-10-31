from exotel import Exotel 
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

import os
import sys
import requests

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'zi-t\xaa\xc7\xf0.\xdb\xc3\xed\xc0}$\xbaL\xa1\xa6\xb1\xd5'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/qa', methods=['GET'])
def ques():
    return render_template('qa.html')

@app.route('/experts', methods=['GET'])
def experts():
    return render_template('experts.html')

@app.route('/calldata', methods=['GET','POST'])
def call():
	base = "https://non56:eedaef1428bfc46e254134be41cd5380b85ccc56@twilix.exotel.in/v1/Accounts/non56/Calls/connect"
	from_num = "%011d"% (9560894192) 
	call_id  = "%011d"% (9243422233)
	data = {
            'From': from_num,
            'CallerId': call_id,
            'Url': "http://my.exotel.in/exoml/start/56743",
            'StatusCallback':'http://localhost:5000/calldata'
    }

	x  = requests.post(base,data)
	print x
	return render_template('data.html')

# When developing locally, this will use port 5000, 
# in production Heroku will set the PORT environment variable.    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

