
class Node(object):
	#val: value stored in node
	#predecessor: node preceding self
	def __init__(self, val=None, predecessor=None):
		self.val= val
		self.next = None
		#link predecessor node to self
		if predecessor:
			predecessor.next = self
	

class LinkedList(object):
	#_list: optional list to construct LinkedList 
	def __init__(self, _list=None):
		#loop counter for next()
		self.loop = -1
		if _list == None:
			self._list = []
			self.cnt = 0
			#head node initialized to empty node
			self.head = Node()
		else:
			self._list = _list
			self.cnt = 1
			#head node constructed from first elem in _list
			self.head = Node(self._list[0])
			#append elems in _list to head
			for elem in _list[1:]:
				self.append(elem)
	
	def count(self):
		return self.cnt
	
	def __eq__(self, linkedlist):
		if self._list == linkedlist._list:
			#equality based on elems in _list
			return True
		else: 
			return False
			
	def __iter__(self):
		#LinkedList is the iterator
		return self
		
	def __add__(self, _list):
		#construct LinkedList out of joined lists
		_list_list = self._list + _list
		return LinkedList(_list_list)
		
	def __iadd__(self, _list):
		#append elems in list to LinkedList
		for elem in _list:
			self.append(elem)
		return self
		
	def next(self):
		if self.loop == self.cnt-1:
			self.loop = -1
			raise StopIteration
		else:
			self.loop+=1
			return self[self.loop]
			
	def pop(self, index):
		node = self.__getitem(index)
		if index ==0: 
			#unlink head
			self.head = self.head.next
		elif index == self.cnt-1:
			#unlink tail node
			self.__getitem(index-1).next = None
		else: 
			#unlink sandwhiched node
			node = node.next 
		self.cnt-=1
		return node.val
		
	def __getitem(self, index):
	   #node is a copy of the head node
		node = Node(self.head.val, None)
		node.next = self.head.next
		try:
			#follow node trail up to index
			if index != 0:
				for i in range(index):
					node= node.next
				return node
		except AttributeError:
			raise IndexError
		else: return self.head 
	
	def __getitem__(self, index):
		return self.__getitem(index).val
		
	def append(self, elem):
		if self.cnt == 0:
			#head node takes the elem
			self.head = Node(elem)
		else: 
			#link the end of the list up with the elem
			node = Node(elem, self.__getitem(self.cnt-1))
		self.cnt+=1
		
l = LinkedList()

l.append(2)
print l.count()  # Should return 1
print l._list
m = l + [2, 3]     # Should return [1, 2, 3] but not mutate the original list
l += [3, 4]   # Should return None and append [3, 4] to the original list

print "l"
for i in l: print i
print "m"
for i in m: print i