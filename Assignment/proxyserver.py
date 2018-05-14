from flask import Flask, jsonify, request
from requests import get
from flask_caching import Cache
import json
import logic, settings

# from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('ssl.key')
# context.use_certificate_file('ssl.crt')


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})



@app.route("/whales", methods = ['POST'])
def updateWhale(): 
	whale = request.get_json(silent=True)
	if logic.updateWhale(whale):
		return 'Succesful'
	return 'Unsuccesful'


@app.route("/whales", methods = ['GET'])
def getWhales():
	whales = cache.get('whales')
	if whales is None:
		settings.cache_miss_count += 1
		whales = logic.getWhales().decode('utf-8')
		whales = json.loads(whales)
		cache.set('whales',whales,timeout=5*60)
	else:
		settings.cache_hit_count += 1
	return jsonify(whales)


@app.route("/whale/<int:id>", methods = ['GET'])
def getWhale(id):
	whales = cache.get('whale'+str(id))
	if whales is None:
		settings.cache_miss_count += 1
		whale = logic.getWhale(id).decode('utf-8')
		whale = json.loads(whale)
		cache.set('whale'+str(id),whale,timeout=5*60)
	else:
		settings.cache_hit_count += 1
	whale = cache.get('whale'+str(id))
	return jsonify(whale)


@app.route("/whales/purge", methods = ['PURGE'])
def purgeCache():
	settings.clear()
	return 'purge succesful'


@app.route("/whales/sync", methods = ['POST'])
def syncCache():
	cache_whales = cache.get('whales')
	if cache_whales is None:
		cache_whales = logic.getWhales().decode('utf-8')
		cache_whales = json.loads(cache_whales)
		cache.set('whales',cache_whales,timeout=5*60)
		return 'Sync Succesful'
	
	api_whales = logic.getWhales().decode('utf-8')
	api_whales = json.loads(api_whales)
	print(cache_whales)
	print(api_whales)
	if cache_whales == api_whales:
		return 'The cache has the latest data'
	else:
		cache_whales = logic.getWhales().decode('utf-8')
		cache_whales = json.loads(cache_whales)
		cache.set('whales',cache_whales,timeout=5*60)
		return 'Sync Succesful'


if __name__ == "__main__":
	app.run(debug=True, port = 5000, ssl_context = ('cert/cert.pem','cert/key.pem') )


