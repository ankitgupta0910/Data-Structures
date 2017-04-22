import math

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

    def get_next(self):
        # type: () -> object
        return self.next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.get_next():
                temp = temp.get_next()
            temp.set_next(new_node)

    def traverse(self):
        current = self.head
        while current:
            print (current.get_data())
            current = current.get_next()

    def traverse_rec(self, head1):
        current = head1
        if current:
            print current.get_data()
            self.traverse_rec(current.get_next())

    def middle(self):
        m = 1
        n = 1
        i = 0
        p1 = self.head
        p2 = self.head
        while p2.get_next() is not None:
            if i is 0:
                p2 = p2.get_next()
                i = 1
                n += 1
            else:
                p1 = p1.get_next()
                p2 = p2.get_next()
                m += 1
                n += 1
                i = 0
        # print math.floor(n/2)
        print p1.get_data()

hello = LinkedList()
hello.insert(10)
hello.insert(20)
hello.insert(30)
hello.insert(40)
hello.insert(50)
hello.insert(60)
hello.insert(70)
hello.insert(80)
# hello.insert(90)

# hello.traverse()
# hello.reverse_rec(hello.head)
# hello.traverse()
hello.middle()
