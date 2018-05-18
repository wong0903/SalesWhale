from flask import jsonify
import http.client
import ssl, json

from config import TOKEN

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)

# TESTED
# return: true/false
def updateWhale(whale):
	conn = http.client.HTTPSConnection('whalemarket.saleswhale.io', context = ssl_context)
	headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+ TOKEN}
	params = json.dumps(whale)
	conn.request('POST', '/whales', body = params, headers = headers)
	response = conn.getresponse()
	data = response.read()
	print(data)
	conn.close()
	#convert bytes to string
	my_str = data.decode('utf-8')
	#convert string to dict
	whale = json.loads(my_str)
	if list(whale)[0] == 'error':
		return False
	return True

# return string of dict (contains '\n')
def getWhales():
	conn = http.client.HTTPSConnection('whalemarket.saleswhale.io', context = ssl_context)
	headers = {'Authorization': 'Bearer ' + TOKEN}
	conn.request('GET','/whales', headers = headers)
	res = conn.getresponse()
	data = res.read()
	conn.close()
	return data.decode('utf-8')

# return string of dict (contains '\n')
# 'error' in dict if not found
def getWhale(id):
	conn = http.client.HTTPSConnection('whalemarket.saleswhale.io', context = ssl_context)
	headers = {'Authorization': 'Bearer '+ TOKEN}
	conn.request('GET','/whales/' + str(id), headers = headers)
	res = conn.getresponse()
	data = res.read()
	conn.close()
	return data.decode('utf-8')

def calculateHitRatio(cache_hit, cache_miss):
	hit_ratio = cache_hit/(cache_hit + cache_miss)
	return hit_ratio

 




