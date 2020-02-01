
# Node class  
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.perv = None 
class LinkedList: 
    def __init__(self): 
        self.head = None
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node
    def deleteNode(self, key): 
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next 
        if(temp == None): 
            return 
        prev.next = temp.next 
        temp = None 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (" %d" %(temp.data),) 
            temp = temp.next
  

llist = LinkedList()
llist.push(1)
llist.push(8)
# pushing 9 in 3rd position
llist.push(9)
llist.push(7) 
llist.push(6) 
llist.push(2)

print ("Created Linked List: ")
llist.printList() 
llist.deleteNode(9)  
print ("\nLinked List after Deletion of 1:")
llist.printList()
class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return True 
            current = current.next
        return False 
if __name__ == '__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.push(1)
    llist.push(8)
    llist.push(9)
    llist.push(7) 
    llist.push(6) 
    llist.push(2)
  
    if llist.search(9): 
        print("Yes") 
    else: 
        print("No") 
    if llist.search(12):
        print("Yes") 
    else: 
        print("No") 

class node:
    def __init__(self,data=None):
        self.data=data
        self.nextnode=None
        self.prevnode=None

x1=node("2")
x2=node("6")
x3=node("7")
x4=node("8")
x5=node("1")
x6=node("")

# SLL
x1.nextnode=x2
x2.nextnode=x3
x3.nextnode=x4
x4.nextnode=x5
print("SLL:")
head=x1
while head:
    print(head.data)
    head=head.nextnode
x5.nextnode=x1
x1.prevnode=x5
x1.nextnode=x2
x2.nextnode=x3
x2.prevnode=x1
x3.nextnode=x4
x3.prevnode=x2
x4.nextnode=x5
x4.prevnode=x3


currentnode = x5
print("CLL node")
while currentnode:
    print (currentnode.data)
    if currentnode.data == '8':
        break
    currentnode = currentnode.nextnode

print("update node 3")
index = 1
currentnode = x5
while currentnode:
    if index ==3:
        currentnode.data = '9'
        index +=1
        print (currentnode.data)
        if currentnode.data =='8':
            break
        currentnode=currentnode.nextnode
print ("traverse Forword")
currentnode=x5
while currentnode:
    print(currentnode.data)
    if currentnode.data =='8':
        break
    currentnode=currentnode.nextnode

print ("traverse Backword")
currentnode=x4
while currentnode:
    print(currentnode.data)
    if currentnode.data =='1':
        break
    currentnode=currentnode.prevnode
    
