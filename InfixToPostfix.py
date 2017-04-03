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

precedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}


def has_higher_precedence(op1, op2):
        if precedence[op1] > precedence[op2]:
            return True
        elif precedence[op1] < precedence[op2]:
            return False
        else:
            return True

new_stack = Stack()
exp = "A+B*C-D*E"
new_exp = ""
for i in exp:
    if i.isalpha():
        new_exp = new_exp + i
    else:
        while new_stack.top is not -1 and has_higher_precedence(new_stack.stack[-1], i):
            new_exp = new_exp + new_stack.pop()
            # new_stack.top -= 1
        new_stack.push(i)

while new_stack.top is not -1:
    new_exp = new_exp + new_stack.pop()

print new_exp
