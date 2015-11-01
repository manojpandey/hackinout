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
app.config['SECRET_KEY'] = '6d4c14c8e3d89221cb470b0b2f03e044'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'hackinout'

@app.route('/')
@app.route('/index.html', methods=['GET','POST'])
def main():
    return render_template('index.html')

@app.route('/login.html', methods=['GET'])
@app.route('/login', methods=['GET'])

def login():
    
    return render_template('login.html')


@app.route('/signup.html', methods=['GET'])
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@app.route('/view.html', methods=['GET'])
@app.route('/view', methods=['GET'])
def view():
    return render_template('view.html', answer = 'query123')

@app.route('/submit.html', methods=['GET'])
@app.route('/submit', methods=['GET'])
def submit():
    return render_template('submit-ans.html')

@app.route('/qa', methods=['GET'])
def ques():

    return render_template('qa.html')

@app.route('/viewqa', methods=['GET', 'POST'])
def viewqa():
    return render_template('view-qa.html')

@app.route('/viewqasked', methods=['GET', 'POST'])
def viewqasked():
    base = "https://non56:eedaef1428bfc46e254134be41cd5380b85ccc56@twilix.exotel.in/v1/Accounts/non56/Calls/connect"
    from_num = "%011d"% (9560894192) 
    call_id  = "%011d"% (9243422233)
    data = {
            'From': from_num,
            'CallerId': call_id,
            'Url': "http://my.exotel.in/exoml/start/56743",
            'StatusCallback': 'http://3f0cd17e.ngrok.io/calldata'
    }

    x  = requests.post(base,data)
    print x
    return render_template('view-qa-asked.html')


def show_posts():
    posts = []
    for account in stormpath_manager.application.accounts:
        if account.custom_data.get('posts'):
            posts.extend(account.custom_data['posts'])

    posts = sorted(posts, key=lambda k: k['date'], reverse=True)
    return render_template('show_posts.html', posts=posts)


# @app.route('/call', methods=['GET','POST'])
# def call():
# 	base = "https://non56:eedaef1428bfc46e254134be41cd5380b85ccc56@twilix.exotel.in/v1/Accounts/non56/Calls/connect"
# 	from_num = "%011d"% (9560894192) 
# 	call_id  = "%011d"% (9243422233)
# 	data = {
#             'From': from_num,
#             'CallerId': call_id,
#             'Url': "http://my.exotel.in/exoml/start/56743",
#             'StatusCallback': 'http://3f0cd17e.ngrok.io/calldata'
#     }

# 	x  = requests.post(base,data)
# 	print x
# 	return render_template('view-qa-asked.html')

@app.route('/calldata', methods=['GET', 'POST'])
def callback():
	return render_template('data.html')

# When developing locally, this will use port 5000, 
# in production Heroku will set the PORT environment variable.    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
