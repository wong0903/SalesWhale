from werkzeug.contrib.cache import SimpleCache
from flask import Flask, jsonify, request
import json

import cache_logger
import logic

app = Flask(__name__)
cache = SimpleCache()
cache_logger = cache_logger.Cache_Logger()

# werkzeug caching
# http://werkzeug.pocoo.org/docs/0.14/contrib/cache/

@app.route('/')
def hello():
    return 'Hello, World!'

# update whale
@app.route("/whales", methods = ['POST'])
def updateWhale(): 
	whale = request.get_json(silent=True)
	if logic.updateWhale(whale):
		return 'Succesful'
	return 'Unsuccessful'

# get all whales
@app.route("/whales", methods = ['GET'])
def getWhales():
	whales = logic.getWhales()
	whales = json.loads(whales)
	return jsonify(whales)


# get whale by id
@app.route("/whale/<int:id>", methods = ['GET'])
def getWhale(id):
	whales = cache.get('whale_' + str(id))
	if whales is None:
		cache_logger.miss()
		whale = logic.getWhale(id)
		whale = json.loads(whale)

		# if not found in the main server
		if('error' in whale):
			return jsonify(whale)

		cache.set('whale_' + str(id), whale, timeout=5*60)
	else:
		cache_logger.hit()

	whale = cache.get('whale_' + str(id))

	return jsonify(whale)


# purge cache
@app.route("/whales/purge", methods = ['GET'])
def purgeCache():
	cache.clear()
	return 'purge succesful'

# sync cache
@app.route("/whales/sync", methods = ['GET'])
def syncCache():	
	list_whales_id = list(cache.__dict__['_cache'].keys())

	if not list_whales_id:
		return 'Cache is empty'
	else:
		for id in list_whales_id:
			id = id[-2:]
			print(id)
			whale_api = logic.getWhale(id)
			whale_api = json.loads(whale_api)
			whale_cache = cache.get('whale_' + str(id))
			print(whale_api)
			print(whale_cache)
			if whale_cache != whale_api:
				cache.set('whale_' + str(id), whale_api, timeout=5*60)
			else:
				continue
		return 'Cache is updated'

# calculate the cache hit ratio
@app.route("/whales/cache_info", methods = ['GET'])
def getCacheHitRatio():
	hit_ratio = 0
	cache_info = {'cache_hit':cache_logger.hit_count, 'cache_miss':cache_logger.miss_count}
	if cache_info['cache_hit'] != 0 and cache_info['cache_miss'] != 0:
		hit_ratio = logic.calculateHitRatio(cache_info['cache_hit'], cache_info['cache_miss'])
	return ('The cache hit ratio is {:.2f}'.format(hit_ratio))
		
								
# main logic
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)


