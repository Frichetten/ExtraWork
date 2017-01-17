import sys
from time import sleep

class loadingBar:
	def __init__(self, total):
		self.index = 0
		self.total = total

	def __iter__(self):
		return self

	def __next__(self):
		if self.index < self.total:
			self.index += 1
			index = self.index

			length = 30
			negSpace = int(index /(self.total/length))
			space = length-negSpace
			percent = int(index/self.total*100)

			print('\r', end='')
			print('[{0}{1}] {2}%'.format('\u2588'*negSpace, 
				' '*(space), 
				percent), end='')

			sleep(0.1)
			return index
		else:
			raise StopIteration()

a = [x for x in range(50)]
b = loadingBar(len(a))
for y in b:
	None

print()
