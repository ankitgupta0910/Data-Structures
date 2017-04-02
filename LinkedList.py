class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

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

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next1 = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = next1
        self.head = prev

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
hello.reverse()
hello.traverse()
