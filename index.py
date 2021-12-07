import IITB_SSO
from flask import Flask,request
from werkzeug.utils import redirect
app = Flask(__name__)

@app.route('/')
def new():
	finalData = IITB_SSO.ssoVerification(request)
	return finalData

if __name__ == '__main__':
	app.run(debug=True)