from flask import jsonify
import http.client, urllib.parse
import ssl, json
from config import TOKEN

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)

def updateWhale(whale):
	conn = http.client.HTTPSConnection('whalemarket.saleswhale.io', context = ssl_context)
	headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+ TOKEN}
	params = json.dumps(whale)
	conn.request('POST', '/whales', body = params, headers = headers)
	response = conn.getresponse()
	data = response.read()
	conn.close()
	my_str = data.decode('utf-8')
	whale = json.loads(my_str)
	if list(whale)[0] == 'error':
		return False
	return True

def getWhales():
	print('haha')
	conn = http.client.HTTPSConnection('whalemarket.saleswhale.io', context = ssl_context)
	headers = {'Authorization': 'Bearer ' + TOKEN}
	conn.request('GET','/whales',headers = headers)
	res = conn.getresponse()
	data = res.read()
	conn.close()
	return data

def getWhale(id):
	print('in')
	conn = http.client.HTTPSConnection('whalemarket.saleswhale.io', context = ssl_context)
	headers = {'Authorization': 'Bearer '+ TOKEN}
	conn.request('GET','/whales/'+str(id), headers = headers)
	res = conn.getresponse()
	data = res.read()
	conn.close()
	return data

 




