#task no 1,
#Reg no 13763
#Zubair Usman

"""

progrem writen for adding two Matrix 3x3
    which is given by the user ..

def addMatrix(m1,m2):
    finalmatrix = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            finalmatrix[i][j] = m1[i][j] + m2[i][j]
    return finalmatrix
matrix1=eval(input("[+] Enter the first matrix 3*3 : "))
matrix2=eval(input("[+] Enter second matrix 3*3 : "))
matrix=addMatrix (matrix1,matrix2)
print("[=]the sum of matrix : ",matrix)

"""

#Task no 2,

#Single linklist(A)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        
    def addNode(self,n):
        if not self.head:
            self.head=n
        else:
            n.next=self.head
            self.head=n
#Isnert (B)
    def insertNode(self,pos,n):
        if pos == 1:
            n.next = self.head
            self.head = n
            return
        bb = self.head
        nodeId = 1
        while bb:
            if nodeId+1 == pos:
                n.next = bb.next
                bb.next = n
            bb = bb.next
            nodeId+=1

#Delete (C)
    def deleteNode(self,pos):
        if pos == 2:
            self.head = self.head.next
            return
        bb = self.head
        while bb:
            bb = bb.next
#Display (D)            
    def display(self):
        bb=self.head
        while bb:
            print(bb.data)
            bb=bb.next
            
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

list1=linkedlist()
list1.addNode(node1)
list1.addNode(node2)
list1.addNode(node3)
list1.addNode(node4)
print("List")
list1.display()
print("------------------------------------------------------------------------------------")
list1.deleteNode(2)
print("List after Deleted Node")
list1.display()
print("------------------------------------------------------------------------------------")
list1.insertNode(2,node4)
print("List after Inserting Node")
list1.display()


"""

N = 4
   

def reverseDiagonal(array): 
  
    i = 0
    j = N 
    while (i < j) : 
   
        array[i][i], array[j - 1][j - 1] = array[j-1][j-1], array[i][i] 

        array[i][j - 1], array[j - 1][i] = array[j-1][i], array[i][j-1] 
   
        i += 1
        j -= 1

    for i in range(N): 
        for j in range( N): 
            print( array[i][j],end="  ") 
        print() 

if __name__ == "__main__": 
      
    matrix = [[ 1, 2,  3,  4], 
                        [5, 6,  7,  8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16 ]] 
    reverseDiagonal(matrix) 


"""





