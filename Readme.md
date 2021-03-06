# Installation
This package is available on pypi.org can be directly installed using pip
```
pip install IITB-SSO
```
# How to get clientId and clientSecret
- Register a new aplication and copy the Client ID and Client Secret [Here](https://gymkhana.iitb.ac.in/profiles/oauth/applications/register/)
- Credentials token is base64 of ClientId:ClientSecret can be generated [Here](https://www.base64encode.org/)
### Example
```
Client Id: wewaG9BBobp9FAKEoQ5EP2AfDQ86XIgT9iCroJ9p
```
```
Client Secret : C4xlSTYYeY46UfHYlnFAKE922PtvNBevv3wivJfuHylGKlHxrdJBk8HhDOEm005Cr2CHxTyiqoOphnT547YXWi4f9LaI6oqRO1i9kGRYOcAbGpQb2FWeXLonJvvCQMdkO
```
```
Decoded base64 : wewaG9BBobp9FAKEoQ5EP2AfDQ86XIgT9iCroJ9p:C4xlSTYYeY46UfHYlnFAKE922PtvNBevv3wivJfuHylGKlHxrdJBk8HhDOEm005Cr2CHxTyiqoOphnT547YXWi4f9LaI6oqRO1i9kGRYOcAbGpQb2FWeXLonJvvCQMdkO
```
```
Encoded base64 : d2V3YUc5QkJvYnA5RkFLRW9RNUVQMkFmRFE4NlhJZ1Q5aUNyb0o5cDpDNHhsU1RZWWVZNDZVZkhZbG5GQUtFOTIyUHR2TkJldnYzd2l2SmZ1SHlsR0tsSHhyZEpCazhIaERPRW0wMDVDcjJDSHhUeWlxb09waG5UNTQ3WVhXaTRmOUxhSTZvcVJPMWk5a0dSWU9jQWJHcFFiMkZXZVhMb25KdnZDUU1ka08=
```
```
CREDENTIALS_TOKEN : "Basic d2V3YUc5QkJvYnA5RkFLRW9RNUVQMkFmRFE4NlhJZ1Q5aUNyb0o5cDpDNHhsU1RZWWVZNDZVZkhZbG5GQUtFOTIyUHR2TkJldnYzd2l2SmZ1SHlsR0tsSHhyZEpCazhIaERPRW0wMDVDcjJDSHhUeWlxb09waG5UNTQ3WVhXaTRmOUxhSTZvcVJPMWk5a0dSWU9jQWJHcFFiMkZXZVhMb25KdnZDUU1ka08="
```
## Sample usage:
#### .env
```
CLIENT_ID = "<Your Client id here>"
CLIENT_SECRET_CODE = "<Your Secret Code>"
REDIRECT_URI = "http://127.0.0.1:5000/"
SSO_URL="https://gymkhana.iitb.ac.in/profiles/oauth/authorize/"
CREDENTIALS_FETCH_URL = "https://gymkhana.iitb.ac.in/profiles/oauth/token/"
CREDENTIALS_TOKEN = "Basic <Credenticals Token>"
DATA_URL = "https://gymkhana.iitb.ac.in/profiles/user/api/user/"
SCOPE = "ldap profile basic sex" 
```

#### index.py
```
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
```