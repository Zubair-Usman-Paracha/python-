print ("Name : Zubair Usman ")
print ("Reg no : 13763")
print ("Final term Lab Exam ...")

print ("--------------- ( Queue List ) ---------------")
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.create()
    def create(self):
        self.head=None
        self.tail=None
    def enqueue(self,data):
        data=node(data)
        if self.head is None:
            self.head=data
        else:
            self.tail.next=data
        self.tail=data
    def dequeue(self):
        data=self.head.data
        self.head=self.head.next
        return data
    def isEmpty(self):
        if self.head:
            print("Queue is not Empty.")
        else:
            print("Queue is Empty.")
    def display(self):
        datas=[]
        head=self.head
        while head:
            datas.append(head.data)
            head=head.next
        return datas
    
q=queue()
print("checking queue is empty or not:")
q.isEmpty()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.display())
q.dequeue()
print(q.display())
q.enqueue(15)
print(q.display())
q.isEmpty()

