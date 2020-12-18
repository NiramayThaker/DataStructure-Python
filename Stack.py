class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit
    
    # for printing stack
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # for pushing an element to stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)

    # for popping the uppermost element
    def pop(self):
        if len(self.stack) <= 0:
            return "Stack empty"
        else:
            return self.stack.pop()

    # for peeking(looking) the top-most element of the stack
    def peek(self):
        if len(self.stack) <= 0:
            return "Stack empty"
        else:
            return self.stack[len(self.stack) - 1]

    # to check weather stack is empty or not 
    def checkEmpty(self):
        return self.stack == []

    # to check the size of stack
    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    MyStack = Stack()                                        #Creating object of stack class
    for i in range(10):
        MyStack.push(i)
    print(MyStack)
    MyStack.pop()                                            # popping the top element
    MyStack.push(90)
    MyStack.push(125)
    print(MyStack)
    MyStack.pop()
    print(MyStack)
    print(MyStack.peek())                                     # Print the top-most(1st) element of the stack
    print("Is stack empty ..? -> ", MyStack.checkEmpty())     # Will cheak weather stack is empty or not
    print(MyStack.size())                                     # Print the size if the stack
