"""
Bonus
speedtest - Shows the api retrieval time
"""

from urllib.parse import urlparse
import http.client, ssl
import json, time, random
import cache_logger

proxyip = 'localhost'

#################### HELPER METHOD ##################################

# return: {'whales': <list of whales>}
def get_all_whales():
	conn = http.client.HTTPConnection(proxyip, port=5000)
	conn.request('GET','/whales')
	res = conn.getresponse()
	data = res.read()
	conn.close()
	return json.loads(data.decode('utf-8'))

# should be used prior to test case execution
# return: <list: all existing whale id>
def get_all_id():
	list_whales = get_all_whales()['whales']
	list_whales_id = [i['id'] for i in list_whales]
	return list_whales_id


###################### TEST CASE ####################################

def speed_test():

	list_whales_id = get_all_id()

	start_time = time.time()	# start time

	conn = http.client.HTTPConnection(proxyip, port=5000)
	#Do twice- first time for direct access, second time for cache access
	for i in range(2):
		for j in list_whales_id:		# loop for every whales id
			conn.request('GET','/whale/' +  str(j))
			res = conn.getresponse()
			data = res.read()
	conn.close()

	total_time = (time.time() - start_time)	# end time
	average_time = (total_time/ len(list_whales_id))

	print('[SPEED TEST]')
	print('Number of API call:\t{}'.format(len(list_whales_id)))
	print('Total time:\t{}s'.format(total_time))
	print('Average time:\t{}s'.format(average_time))

	return


def speed_test_with_noise():
	'''add some noise to that id list and follow speed_test()'''
	list_whales_id = get_all_id()

	#Randomized insert 5 unique ids into the list
	list_whales_id.extend(random.sample(range(1,100),5))

	#Remove any duplicates in the list
	my_set = {*list_whales_id}
	list_whales_id = [*my_set]

	start_time = time.time()	# start time

	conn = http.client.HTTPConnection(proxyip, port=5000)
	for i in range(2):
		for j in list_whales_id:		
			conn.request('GET','/whale/' +  str(j))
			res = conn.getresponse()
			data = res.read()
	conn.close()

	total_time = (time.time() - start_time)	# end time
	average_time = (total_time/ len(list_whales_id))

	print('[SPEED TEST WITH NOISE]')
	print('Number of API call:\t{}'.format(len(list_whales_id)))
	print('Total time:\t{}s'.format(total_time))
	print('Average time:\t{}s'.format(average_time))
	return


if __name__ == "__main__":
	speed_test()
	#speed_test_with_noise()

