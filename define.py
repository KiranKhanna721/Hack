import requests
import json

#GET "https://graph.facebook.com/{api-endpoint}&access_token={your-app_id}|{your-app_secret}"

def getCreds():
    creds = dict()
    creds['access_token'] = 'EAAGC2HBVGEcBAIma5uTpXruw47Wb66LscuxQSqgvLQHjjGhpy1TzbL6OzxErsBtYInDQmQSn3cwj1HSzjLD7Jm1cAViT5LM6Cni8KVo2LiTAYhlnJqLuXiwCfSzNsp64i91KUR9ThEemko5vqlNKy9zPjaH1rsonpm5mQROTDy8NqiVwMJrh7AxNIpeAnblsvf46egZDZD',
    creds['app_id'] = '425341085882439',
    creds['app_secret'] = 'ddc673702c46f0b17d54fcad4f62a2bd',
    creds['graph_domain'] = "https://graph.facebook.com/"
    creds['graph_version'] =  "v12.0"
    creds['endpoint_base'] = creds['graph_domain']+creds['graph_version']
    creds['debug'] = 'no'

	

    return creds


def APIcall( url, endpointParams, debug = 'no' ) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print ("\nURL: ") # title
	print (response['url']) # display url hit
	print ("\nEndpoint Params: ") # title
	print (response['endpoint_params_pretty']) # display params passed to the endpoint
	print ("\nResponse: ") # title
	print (response['json_data_pretty']) # make look pretty for cli