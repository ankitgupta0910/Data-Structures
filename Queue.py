class Queue(object):
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.front is -1 and self.rear is -1:
            self.front += 1
            self.rear += 1
            print "Element %d is inserted in Queue at position %d" % (data, self.rear)
            self.queue.insert(self.rear, data)
        else:
            self.rear += 1
            print "Element %d is inserted in Queue at position %d" % (data, self.rear)
            self.queue.insert(self.rear, data)

    def dequeue(self):
        if self.front is -1:
            print "queue is Empty"
        elif self.front is self.rear:
            print "Element %d is deleted from queue from position %d" % (self.queue[self.front], self.front)
            self.front = -1
            self.rear = -1
        else:
            print "Element %d is deleted from queue from position %d" % (self.queue[self.front], self.front)
            self.front += 1

    def traverse(self):
        if self.front is -1:
            print "queue is Empty"
        else:
            temp = self.front
            while temp <= self.rear:
                print "Element %d is present in queue at position %d" % (self.queue[temp], temp)
                temp += 1

new_queue = Queue()
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)
new_queue.enqueue(50)
new_queue.traverse()
new_queue.dequeue()
new_queue.traverse()
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)
new_queue.enqueue(50)
new_queue.traverse()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.traverse()
print "Hello"
