import pickle


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
 
 
def insert(node, key):
 
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    return node
 
 
def minValueNode(node):
    current = node
 
    while(current.left is not None):
        current = current.left
 
    return current


def search(root, key): 
    if root is None or root.key == key: 
        return root 
  
    if root.key < key: 
        return search(root.right, key) 
    
    return search(root.left, key) 
	
 
def deleteNode(root, key):
    if root is None:
        return root
 
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    else:
 
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        temp = minValueNode(root.right)
 
        root.key = temp.key
 
        root.right = deleteNode(root.right, temp.key)
 
    return root

 
def dump_tree(root):
	if root:
		with open('tree_res.pickle', 'wb') as ouf:
			return pickle.dump(root, ouf)


try:
	with open('tree_res.pickle', 'rb') as inf:
		tree = pickle.load(inf)
	print('Reserve copy uploaded successfully.')
	
except FileNotFoundError as err:
	print(err)
	print('Creating empty tree...')
	tree = None

except:
	print('Problems with reserve file!')
	print('Creating empty tree...')
	tree = None

while True:
	req = input().split()
	if req[0] == 'add':
		tree = insert(tree, int(req[1]))
	if req[0] == 'find':
		print(search(tree, int(req[1])))
	if req[0] == 'delete':
		tree = deleteNode(tree, int(req[1]))
	if req[0] == 'print':
		inorder(tree)
	if req[0] == 'clear':
		tree = None
		print('The tree is cleared')
	if req[0] == 'dump':
		dump_tree(tree)
		print('Reserve copy created successfully.')
	if req[0] == 'exit':
		break