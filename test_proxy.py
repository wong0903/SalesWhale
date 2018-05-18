import json, pytest
from config import TOKEN
import proxyserver, logic

'''Configures the application for testing'''
@pytest.fixture
def client():
	proxyserver.app.config['TESTING'] = True
	client = proxyserver.app.test_client()
	yield client

'''Test updateWhale()'''
def test_update(client):
	mimetype = 'application/json'
	headers = {
	'ContentType': mimetype,
	'Authorization': 'Bearer '+ TOKEN
	}

	#Existing whale
	whale = {"name": "orca", "country": "Atlantis" }

	# New whale - Succesful
	# whale = {"name": "Giant Whale", "country": "India"}

	response = client.post('/whales', json = whale , headers = headers)
	assert response.status_code == 200
	assert b'Unsuccessful' in response.data

'''Test getWhale(id)'''
def test_getWhale(client):

	#Existing whale
	path = '/whale/10'

	#Non-existing whale
	#path = '/whale/11'

	response = client.get(path)

	assert response.status_code == 200
	assert 'whale' == list(response.get_json().keys())[0]
	#Comment it if testing non-existing whale
	assert 10 == response.get_json()['whale']['id']

'''Test getCacheHitRatio'''
def test_calculateHitRatio():
	cache_hit = 5
	cache_miss = 5
	hit_ratio = logic.calculateHitRatio(cache_hit,cache_miss)
	assert hit_ratio == 0.5