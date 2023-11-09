class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.k = k
        self.size = 0
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        
        self.q[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.k

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        print(self.q[self.head])
        self.q[self.head] = None
        self.head = (self.head + 1) % self.k

        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.q[self.head]
        return -1

    def Rear(self) -> int:
        if self.isEmpty(): 
            return -1
        return self.q[self.tail - 1]

    def isEmpty(self) -> bool:
        if self.size == 0: return True
        return False
        
    def isFull(self) -> bool:
        if self.size == self.k: return True
        return False
    
    def show_q(self) -> None:
        print(self.q)


if __name__ == '__main__':
    q = MyCircularQueue(10)
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    
    q.show_q()    
    
    q.deQueue()
    q.deQueue()
    
    q.show_q()    
    
    print("rear: ", q.Rear())
    print("front: ", q.Front())
