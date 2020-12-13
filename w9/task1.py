class BinTree:

	def __init__(self, data):

		self.left = None
		self.right = None
		self.data = data
		self._iter()
		
	def _iter(self):
		self.tree = iter(self.dfs_binary_tree(self))
	
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = BinTree(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = BinTree(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
		self._iter()
		
	def dfs_binary_tree(self, root):
		result = []
		if root:
			result.append(root.data)
			result += self.dfs_binary_tree(root.left)
			result += self.dfs_binary_tree(root.right)
		return result
		
	def tree_print(self):
		if self.left:
			self.left.tree_print()
		print(self.data)
		if self.right:
			self.right.tree_print()
	
	def __iter__(self):
		return self
		
	def __next__(self):
		return next(self.tree)

if __name__ == '__main__':
	root = BinTree(12)
	root.insert(6)
	root.insert(14)
	root.insert(3)
	for i in root:
		print(i)
