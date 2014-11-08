from jawbone.jawbone import Jawbone

client_id="1QcHq0B_THg"
client_secret="70534a74b2f62bbfca58dda2b756ccc9787ccf6b"
redirect_uri="http://www.facebook.com"

jb=Jawbone(client_id,client_secret,redirect_uri,scope='')


#https://pypi.python.org/pypi/jawbone-up/0.1


#default scope is basic_read, set per application 
#space delimited list

jb.auth()
#if error, GET=error
token=jb.access_token(code) #json

#if 200: access_token, token_type, expires_at, refresh_token 

#api_call is generic method for calling any endpoint 
#https://jawbone.com/up/developer/endpoints 

#to get sleep data
endpoint = nudge/api/v.1.0/sleep response = jb.api_call(access_token, endpoint)
#response is json with status_code(200,400,etc)
#parse for data if response.status==200

