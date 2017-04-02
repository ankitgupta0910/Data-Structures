class Node(object):
    def __init__(self,data):
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

    def delete_front(self):
        self.head = self.head.get_next()

    def delete_end(self):
        temp = self.head
        temp1 = self.head
        while temp1.get_next():
            temp = temp1
            temp1 = temp.get_next()
        temp.set_next(None)

    def delete_mid(self, pos):
        count = 1
        temp = self.head
        temp1 = self.head
        while temp1.get_next() and count is not pos:
            temp = temp1
            temp1 = temp1.get_next()
            count += 1
        temp.set_next(temp1.get_next())

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

hello = LinkedList()
hello.insert(10)
hello.insert(20)
# hello.delete_front()
hello.insert(30)
hello.insert(40)
# hello.delete_mid(2)
# hello.delete_end()
hello.insert(50)
hello.traverse()
# hello.reverse()
# hello.traverse_rec(hello.head)
# hello.traverse_rev_rec(hello.head)
hello.reverse_rec(hello.head)
hello.traverse()
