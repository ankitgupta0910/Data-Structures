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
        print curr.get_data(),
        if curr.get_right() is not None:
            curr1 = curr.get_right()
            self.inorder(curr1)

    def preorder(self, curr):
        print curr.get_data(),
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
        print curr.get_data(),

    def min(self):
        curr = self.root
        while curr.get_left() is not None:
            curr = curr.get_left()
        print "Minimum element is ", curr.get_data()

    def max(self):
        curr = self.root
        while curr.get_right() is not None:
            curr = curr.get_right()
        print "Maximum element is ", curr.get_data()

    def height(self, curr):
        if curr is None:
            return -1
        leftHeight = self.height(curr.get_left())
        rightHeight = self.height(curr.get_right())
        return max(leftHeight,rightHeight) + 1

    def lot(self):
        myq = []
        curr = self.root
        myq.append(curr)
        while myq:
            curr = myq[0]
            # temp = myq[0]
            print curr.get_data(),
            del(myq[0])
            if curr.get_left() is not None:
                myq.append(curr.get_left())
            if curr.get_right() is not None:
                myq.append(curr.get_right())

    def boundary(self, curr):
        if curr.get_left() is not None:
            curr1 = curr.get_left()
            self.boundary(curr1)
        print curr.get_data()
        if curr is self.root:
            while curr.get_right() is not None:
                curr = curr.get_right()
                print curr.get_data()

    def boundary1(self, curr):
        if curr.get_right() is not None:
            curr1 = curr.get_right()
            self.boundary1(curr1)
        if curr.get_left() is not None:
            curr1 = curr.get_left()
            self.boundary1(curr1)
        if curr.get_left() is None and curr.get_right() is None:
            print curr.get_data(),



bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(40)
bst.insert(20)
bst.insert(80)
bst.insert(60)
bst.insert(35)
bst.insert(5)
bst.insert(10)
bst.insert(15)
bst.insert(25)
bst.insert(55)
bst.insert(65)
bst.insert(75)
bst.insert(85)
# bst.boundary(bst.root)
# bst.boundary1(bst.root)
print "Preorder Traversal is: ", bst.preorder(bst.root)
# print "Inorder Traversal is: ", bst.inorder(bst.root)
# print "Postorder Traversal is: ", bst.postorder(bst.root)
# bst.min()
# bst.max()
# print "Height of tree is: ", bst.height(bst.root)
# print "Level Traversal is: ", bst.lot()
