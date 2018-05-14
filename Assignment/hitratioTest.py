import urllib.request
import http.client
import settings
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)


def hit_ratio():
	with open('test','r') as f:
		for line in f:
			print(line)
			conn = urllib.request.urlopen(line, context=ssl_context)
			print(settings.cache_hit_count)
			conn.close()
	print(settings.cache_hit_count)
	hit_ratio = settings.cache_hit_count/(settings.cache_hit_count + settings.cache_miss_count)
	print('The cache hit ratio is {}'.format(hit_ratio))

if __name__ == "__main__":
	hit_ratio()