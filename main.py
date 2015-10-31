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


@app.route('/calldata',method=['GET','POST'])
def call():

    client = Exotel('non56','eedaef1428bfc46e254134be41cd5380b85ccc56')

    from_num = "%011d"% (9560894192) 
    call_id  = "%011d"% (9243422233)


    x  = client.call_flow(from_num,call_id,(56743))
    print x

# When developing locally, this will use port 5000, 
# in production Heroku will set the PORT environment variable.


    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

