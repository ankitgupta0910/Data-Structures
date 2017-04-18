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

    def traverse_rev_rec(self, head1):
        current = head1
        if current is None:
            return
        self.traverse_rev_rec(current.get_next())
        print current.get_data()

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next1 = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = next1
        self.head = prev

    def reverse_rec(self, head1):
        prev = head1
        current = head1.get_next()
        if current.get_next() is None:
            self.head.set_next(None)
            self.head = current
            current.set_next(prev)
            return
        self.reverse_rec(current)
        current.set_next(prev)

    def middle(self):
        m = 1
        n = 1
        p1 = self.head
        p2 = self.head
        while p2.get_next() is not None:
            p1 = p1.get_next()
            p2 = p2.get_next().get_next()
            m += 1
            n += 2
        print math.floor(n/2)

hello = LinkedList()
hello.insert(10)
hello.insert(20)
hello.insert(30)
hello.insert(40)
hello.insert(50)
hello.insert(60)
# hello.traverse()
# hello.reverse_rec(hello.head)
# hello.traverse()
hello.middle()
