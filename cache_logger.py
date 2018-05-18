class Cache_Logger:

	def __init__(self):
		self.hit_count = 0	
		self.miss_count = 0

	def hit(self):
		self.hit_count = self.hit_count + 1
		# print('cache hit!')

	def miss(self):
		self.miss_count = self.miss_count + 1
		# print('cache miss!')

	def clear(self):
		self.hit_count = 0
		self.miss_count = 0