class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def get_data(self):
        return self.data

    def set_prev(self, new_prev):
        self.prev = new_prev

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.get_next() is not None:
                curr = curr.get_next()
            curr.set_next(new_node)
            new_node.set_prev(curr)

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.get_data()
            curr = curr.get_next()

new_list = DoublyLinkedList()
new_list.insert(10)
new_list.insert(20)
new_list.insert(30)
new_list.insert(40)
new_list.insert(50)
new_list.traverse()
