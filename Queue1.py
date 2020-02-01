

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,value):
        self.items.insert(0,value)
    def dequeue(self):
        self.items.pop()
    def printqueue(self):
            print(self.items)
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.printqueue()
print("*********************************")
q.dequeue()
q.printqueue()
