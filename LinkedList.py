class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Atbegin(self,data_in):
        NewNode=node(data_in)
        NewNode.next=self.head
        self.head=NewNode
    def Atend(self,data_in):
        NewNode=node(data_in)
        if (self.head is None):
            self.head=NewNode
        else:
            last=self.head
            while(last.next):
                last=last.next
            last.next=NewNode
    def Atposition(self,position,data_in):
        if (position is None):
            print("position doesnot exit")
            return
        else:
            NewNode=node(data_in)
            NewNode.next=position.next
            position.next=NewNode
    def Display(self):
        CurrentNode=self.head
        while(CurrentNode):
            print(CurrentNode.data)
            CurrentNode=CurrentNode.next
    def Delete(self,Key):
        NewNode=self.head
        if(NewNode is not None):
            if(NewNode.data==Key):
                self.head=NewNode.next
                NewNode=None
                return
        while(NewNode is not None):
            if(NewNode.data==Key):
                break
            prev=NewNode
            NewNode=NewNode.next
        if(NewNode==None):
            return
        else:
            prev.next=NewNode.next
            NewNode=None
