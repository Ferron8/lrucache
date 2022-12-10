
import time


class Node:
	def __init__(self, key, val):
		self.key = key 
		self.val = val
		self.next = None
		self.prev = None



class LRUCache:

	cache_limit = 3

	def __init__(self, func):
		self.func = func
		self.cache = {}
		self.head = Node(0,0)
		self.tail = Node(0,0)
		self.head.next = self.tail
		self.tail.prev = self.head


	def __call__(self, *args, **kwargs):

		if args in self.cache:
			self.llist(args)
			return f'Cached...{self.cache[args]}'

		if len(self.cache) == self.cache_limit:
			node = self.head.next
			self._remove(node)
			del self.cache[node.key]


		results = self.func(*args, **kwargs)
		self.cache[args] = results
		node = Node(args, results)
		self._add(node)
		return results


	def _remove(self, node):
		p = node.prev
		n = node.next
		p.next = n
		n.prev = p

	def _add(self, node):
		p = self.tail.prev
		p.next = node
		self.tail.prev = node
		node.prev = p
		node.next = self.tail



	def llist(self, args):
		current = self.head
		while True:
			if current.key == args:
				node = current
				self._remove(node)
				self._add(node)
				break
			else:
				current = current.next



@LRUCache
def ex_func_01(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n*n


@LRUCache
def ex_func_02(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n*n

print(f'\nFunction: ex_func_01')
print(ex_func_01(4)) # Cache: {(4,): 16}
print(ex_func_01(5)) # Cache: {(4,): 16, (5,): 25}
print(ex_func_01(4)) # Cache: {(5,): 25, (4,): 16}
print(ex_func_01(6)) # Cache: {(5,): 25, (4,): 16, (6,): 36}
print(ex_func_01(7)) # Cache: {(5,): 25, (4,): 16, (6,): 36, (7,): 49}
print(ex_func_01(8)) # Cache: {(4,): 16, (6,): 36, (7,): 49, (8,): 64}

print(f'\nFunction: ex_func_02')
print(ex_func_02(8)) # Cache: {(8,): 64}
print(ex_func_02(7)) # Cache: {(8,): 64, (7,): 49}
print(ex_func_02(6)) # Cache: {(8,): 64, (7,): 49, (6,): 36}
print(ex_func_02(4)) # Cache: {(8,): 64, (7,): 49, (6,): 36, (4,): 16}
print(ex_func_02(5)) # Cache: {(7,): 49, (6,): 36, (4,): 16, (5,): 25}
print(ex_func_02(4)) # Cache: {(7,): 49, (6,): 36, (5,): 25, (4,): 16}


