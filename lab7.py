class StackList:
    def __init__(self,till):
        self.till = till
        self.arr = []
    def push(self,num):
        if len(self.arr) == self.till:
            print("Stack is Full")
            return None
        self.arr.append(num)
        return num
    def pop(self):
        if not len(self.arr):
            print("Stack is Empty")
            return None
        return self.pop()
    def getTop(self):
        if len(self.arr):
            return self.arr[-1]
        print("Stack is Empty")
        return None
    def isEmpty(self):
        if len(self.arr):
            return False
        return True
    def isFull(self):
        if len(self.arr) == self.till:
            return True
        return False
    def display(self):
        for data in self.arr:
            print(data)


s = StackList(5)
print("Is Empty:",s.isEmpty())
print("Is Full:",s.isFull())
print("Pushing:",s.push(20))
print("Pushing:",s.push(2))
print("Pushing:",s.push(4))
print("Top Element",s.getTop())
print("Is Empty:",s.isEmpty())
print("Pushing:",s.push(3))
print("Pushing:",s.push(10))
print("Is Full:",s.isFull())
print("Top Element",s.getTop())
print("Displaying Data")
s.display()
