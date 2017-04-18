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
            print current.get_data(), '->',
            current = current.get_next()

    def reverse(self, head1):
        if head1 is None or head1.get_next() is None:
            return
        else:
            temp = head1.get_next()
            head1.set_next(temp.get_next())
            temp.set_next(head1)
            head1 = temp
            head1.get_next().set_next(self.reverse(head1.get_next().get_next()))
            return head1

hello = LinkedList()
hello.insert(10)
hello.insert(20)
hello.insert(30)
hello.insert(40)
hello.insert(50)
hello.insert(60)
# hello.traverse()
hello.head = hello.reverse(hello.head)
hello.traverse()
