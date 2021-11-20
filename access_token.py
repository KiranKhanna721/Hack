from define import getCreds, APIcall
import datetime

def debugAccessToken( params ) :
	""" Get info on an access token 
	
	API Endpoint:
		https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}
	Returns:
		object: data from the endpoint
	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['input_token'] = params['access_token'] # input token is the access token
	endpointParams['access_token'] = params['access_token'] # access token to get debug info on

	endpointParams['client_id'] = params['app_id']
	endpointParams['client_secret'] = params['app_secret']


	url = str(params['graph_domain']) + 'debug_token?input_token={' + str(endpointParams['input_token']) +"}&access_token={" + str(endpointParams['access_token']) +"}" # endpoint url
	#url = str(params['endpoint_base'])+ '/oauth/access_token?grant_type=' + str(endpointParams['input_token'])+"&client_id{"+str(endpointParams['client_id'])+"}&client_secret={" +str(endpointParams['client_secret'])+"&fb_exchange_token={" + str(endpointParams['input_token']) + "}"
	#url = params['endpoint_base'] + '/oauth/access_token' 

	return APIcall( url, endpointParams, params['debug'] ) # make the api call

params = getCreds() # get creds
params['debug'] = 'yes' # set debug
response = debugAccessToken( params ) # hit the api for some data!


print ("\nData Access Expires at: ") # label
print (datetime.datetime.fromtimestamp( response['json_data']['data']['data_access_expires_at'] ))

print ("\nToken Expires at: " )# label
print (datetime.datetime.fromtimestamp( response['json_data']['data']['expires_at'] )) # display out when the token expires