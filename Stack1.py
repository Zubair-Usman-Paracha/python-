class stack:
    def __init__(self):
        self.item = []
    def push(self,value):
        self.item.append(value)
    def pop(self):
        if self.item<=[0]:
            print("list is empty")
        else:
            self.item.pop()
            
    def display(self):
        print(self.item)
a=stack()
a.push(1)
a.push(2)
a.display()
a.pop()
a.display()
a.pop()
a.display()
a.pop()
