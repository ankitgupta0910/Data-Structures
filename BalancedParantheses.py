class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = -1

    def empty(self):
        if self.top is -1:
            return 0
        else:
            return 1

    def push(self, data):
        self.top += 1
        print "Element %s is pushed in Stack at position %d" % (data, self.top)
        self.stack.append(data)

    def pop(self):
        if self.top is -1:
            print "Stack is Empty"
        else:
            print "Element %s is popped from Stack from position %d" % (self.stack[self.top], self.top)
            self.top -= 1
            return self.stack[self.top+1]

    def traverse(self):
        if self.top is -1:
            print "Stack is Empty"
        else:
            temp = self.top
            while temp is not -1:
                print "Element %d is present in Stack at position %d" % (self.stack[temp], temp)
                temp -= 1


new_stack = Stack()
str = "[{([{)(}])}]"

for i in str:
    if i is "{" or i is "[" or i is "(":
        new_stack.push(i)
    else:
        if i is ")" and new_stack.pop() is "(":
            print "hello"
        else:
            if i is "]" and new_stack.pop() is "[":
                print "hello"
            else:
                if i is "}" and new_stack.pop() is "{":
                    print "hello"
                else:
                    print "Exp is not balanced"
                    exit()

if new_stack.top == -1:
    print "Exp is balanced"
else:
    print "Exp is not balanced"





