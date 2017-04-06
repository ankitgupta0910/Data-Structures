class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        node.set_left(None)
        node.set_right(None)
        if self.root is None:
            self.root = node
        else:
            prev = self.root
            curr = self.root
            while curr is not None:
                if curr.get_data() > data:
                    prev = curr
                    curr = curr.get_left()
                else:
                    prev = curr
                    curr = curr.get_right()
            if prev.get_data() > data:
                prev.set_left(node)
            else:
                prev.set_right(node)

    def inorder(self, curr):
        if curr.get_left() is not None:
            curr1 = curr.get_left()
            self.inorder(curr1)
        print curr.get_data()
        if curr.get_right() is not None:
            curr1 = curr.get_right()
            self.inorder(curr1)

    def preorder(self, curr):
        print curr.get_data()
        if curr.get_left() is not None:
            curr1 = curr.get_left()
            self.preorder(curr1)
        if curr.get_right() is not None:
            curr1 = curr.get_right()
            self.preorder(curr1)

    def postorder(self, curr):
        if curr.get_left() is not None:
            curr1 = curr.get_left()
            self.postorder(curr1)
        if curr.get_right() is not None:
            curr1 = curr.get_right()
            self.postorder(curr1)
        print curr.get_data()

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(40)
bst.insert(20)
bst.insert(80)
bst.insert(60)
bst.preorder(bst.root)
print "\n"
bst.inorder(bst.root)
print "\n"
bst.postorder(bst.root)
