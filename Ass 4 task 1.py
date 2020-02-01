"""
class LinkedList(object): 
    def __init__(self): 
        self.head = None
  
    class Node(object): 
        def __init__(self, d): 
            self.data = d 
            self.next = None
  

    def swapNodes(self, x, y): 
  

        if x == y: 
            return 
  

        prevX = None
        currX = self.head 
        while currX != None and currX.data != x: 
            prevX = currX 
            currX = currX.next
  

        prevY = None
        currY = self.head 
        while currY != None and currY.data != y: 
            prevY = currY 
            currY = currY.next
  

        if currX == None or currY == None: 
            return 

        if prevX != None: 
            prevX.next = currY 
        else: 
            self.head = currY 
  
 
        if prevY != None: 
            prevY.next = currX 
        else:
            self.head = currX 
  
 
        temp = currX.next
        currX.next = currY.next
        currY.next = temp 
  
 
    def push(self, new_data): 
  

        new_Node = self.Node(new_data) 
  

        new_Node.next = self.head 
  

        self.head = new_Node 
  

    def printList(self): 
        tNode = self.head 
        while tNode != None: 
            print (tNode.data) 
            tNode = tNode.next

llist = LinkedList() 
   
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
print ("Linked list before calling swapNodes() ")
llist.printList() 
llist.swapNodes(4, 3)
print ("\nLinked list after calling swapNodes() ")
llist.printList()

"""
"""
# Simple and tail recursive Python program to  
# reverse a linked list 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    def reverseUtil(self, curr, prev): 
          
        # If last node mark it head 
        if curr.next is None : 
            self.head = curr  
              
            # Update next to prev node 
            curr.next = prev 
            return 
          
        # Save curr.next node for recursive call 
        next = curr.next
  
        # And update next  
        curr.next = prev 
      
        self.reverseUtil(next, curr)  
  
  
    # This function mainly calls reverseUtil() 
    # with previous as None 
    def reverse(self): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 
  
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print ("forward linked list")
llist.printList() 
  
llist.reverse() 
  
print ("\nReverse linked list")
llist.printList() 
"""
def printUnion(arr1, arr2, m, n): 
    i,j = 0,0
    while i < m and j < n: 
        if arr1[i] < arr2[j]: 
            print(arr1[i]) 
            i += 1
        elif arr2[j] < arr1[i]: 
            print(arr2[j]) 
            j+= 1
        else: 
            print(arr2[j]) 
            j += 1
            i += 1
  
 
    while i < m: 
        print(arr1[i]) 
        i += 1
  
    while j < n: 
        print(arr2[j]) 
        j += 1
  

arr1 = [1, 2, 4, 5, 6] 
arr2 = [2, 3, 5, 7] 
m = len(arr1) 
n = len(arr2) 
printUnion(arr1, arr2, m, n) 
