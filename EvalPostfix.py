class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.top += 1
        # print "Element %s is pushed in Stack at position %d" % (data, self.top)
        self.stack.insert(self.top, data)

    def pop(self):
        if self.top is -1:
            print "Stack is Empty"
        else:
            # print "Element %d is popped from Stack from position %d" %(self.stack[self.top], self.top)
            self.top -= 1
            temp = self.stack[self.top+1]
            del self.stack[self.top+1]
            return temp

    def traverse(self):
        if self.top is -1:
            print "Stack is Empty"
        else:
            temp = self.top
            while temp is not -1:
                print "Element %s is present in Stack at position %d" %(self.stack[temp], temp)
                temp -= 1

new_stack = Stack()
exp = "23*54*+9-"
new_exp = ""
for i in exp:
    if i.isdigit():
        new_stack.push(i)
    else:
        # while new_stack.top is not -1:
            a = new_stack.pop()
            # print int(a)
            a1 = int(a)
            b = new_stack.pop()
            b1 = int(b)
            if i is "/":
                temp = b1 / a1
            elif i is "*":
                temp = b1 * a1
            elif i is "+":
                temp = b1 + a1
            elif i is "-":
                temp = b1 - a1
            new_stack.push(temp)

print new_stack.pop()
