# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:46:22 2020

@author: Mr ABBAS-TURKI
"""

from flask import Flask
from flask import render_template
from flask import request
import hashlib

# définir le message secret
#MESSAGE_SECRET="hypsilophodon"
app=Flask(__name__)


@app.route("/")
def get_secret_message():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def password():
	if request.method == 'POST':
		user = request.form.get('user')
		password = request.form.get('password')
		if user == "user" and hashlib.sha256(password.encode('utf-8')).hexdigest() == "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8":
			return "Login : hypsilophodon"
		else:
			return "Error"
	else:
		return "Error"

if __name__=="__main__":
    app.run(debug=False, host="0.0.0.0", port=8081, ssl_context=('serveur-cle-publique.pem', 'cle-privee-serveur.pem'))

    #ssl_context=('/etc/letsencrypt/live/mdminhazulhaque.io/fullchain.pem', '/etc/letsencrypt/live/mdminhazulhaque.io/privkey.pem')