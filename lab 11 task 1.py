class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
       
    def EnQueue(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp   

    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
        return str(temp.data)

    def display (self):
        if self.front == None :
            print ("[-] The list is Empty :")
        else :
            self.rear = Node
            print("[+] The Item of the list" ,Node)
  
if __name__== '__main__': 
    q = Queue() 
    q.EnQueue(1) 
    q.EnQueue(7) 
    q.DeQueue() 
    q.DeQueue() 
    q.EnQueue(5) 
    q.EnQueue(2)  
    q.display ()
    print("[-] Dequeued item is " + q.DeQueue()) 
