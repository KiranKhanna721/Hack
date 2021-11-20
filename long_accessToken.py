from define import getCreds, APIcall
import datetime


def longToken(params): 
    endpointParams = dict() # parameter to send to the endpoint
	
    endpointParams['input_token'] = params['access_token'] # input token is the access token
    endpointParams['access_token'] = params['access_token'] # access token to get debug info on
    endpointParams['client_id'] = params['app_id']
    endpointParams['client_secret'] = params['app_secret']

    url=  str(params['endpoint_base'])+ '/oauth/access_token?grant_type=' + str(endpointParams['input_token'])+"&client_id{"+str(endpointParams['client_id'])+"}&client_secret={" +str(endpointParams['client_secret'])+"&fb_exchange_token={" + str(endpointParams['input_token']) + "}"
	#url = params['endpoint_base'] + '/oauth/access_token' 

    return APIcall( url, endpointParams, params['debug'] ) # make the api call

params = getCreds() # get creds
params['debug'] = 'yes' # set debug
response = longToken( params ) # hit the api for some data!

print ("\n ---- ACCESS TOKEN INFO ----\n") # section header
print ("Access Token: ")  # label
print (response['json_data']['access_token'] )# display access token


