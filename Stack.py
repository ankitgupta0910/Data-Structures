class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.top += 1
        print "Element %d is pushed in Stack at position %d" % (data, self.top)
        # self.stack.append(data)
        self.stack.insert(self.top, data)

    def pop(self):
        if self.top is -1:
            print "Stack is Empty"
        else:
            print "Element %d is popped from Stack from position %d" % (self.stack[self.top], self.top)
            del self.stack[self.top]
            self.top -= 1

    def traverse(self):
        if self.top is -1:
            print "Stack is Empty"
        else:
            temp = self.top
            while temp is not -1:
                print "Element %d is present in Stack at position %d" %(self.stack[temp], temp)
                temp -= 1

new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
new_stack.push(50)
new_stack.traverse()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.push(60)
new_stack.traverse()

