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

    def insertAfter(self, prev_node, new_data): 
        if prev_node is None: 
            print ("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data) 
        new_node.next = prev_node.next
        prev_node.next = new_node 

    def append(self, new_data): 
 
        new_node = Node(new_data) 
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
        while (last.next): 
            last = last.next 
        last.next =  new_node
    def searchNode(self,value):
    	curr = self.head
    	id_ = 1
    	results = []
    	while curr:
    		if curr.data == value:
    			results.append(id_)

    		id_+=1
    		curr = curr.next
    	return results

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
        while (temp): 
            print ("%d"%(temp.data))
            
            temp = temp.next
    def getCountRec(self, node): 
        if (not node):
            return 0
        else: 
            return 1 + self.getCountRec(node.next) 

    def getCount(self): 
       return self.getCountRec(self.head)

if __name__ == '__main__':  
    mylist = LinkedList() 
    mylist.append(6) 
    mylist.push(7);  
    mylist.push(1); 
    mylist.append(4)  
    mylist.insertAfter(mylist.head.next, 8) 
    print ("Created linked list is:") 
    mylist.printList()
    mylist.deleteNode(1)  
print ("\nLinked List after Deletion of 1:")
mylist.printList() 
print ("Count of nodes is :",mylist.getCount())
print("Search 8 in given list is on",mylist.searchNode(8))



class Node:
	def __init__(self,value):
		self.data = value
		self.nextNode = None 

	def hasValue(self,value):
		"""Search for value in current Node"""
		return self.data == value

	def getData(self):
		"""Returns current node data"""
		return self.data

	def getNextNode(self):
		"""Returns next node in the current node"""
		return self.nextNode

	def setNextNode(self,node):
		"""Set Next node for the current node"""
		self.nextNode = node
		return True

class Nodes:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def addNode(self,node):
		"""Adding node to end of LinkedList (Nodes)"""
		if not isinstance(node,Node):
			node = Node(node)
		if self.head == None:
			self.head = node
		else:
			self.tail.nextNode = node
		self.tail = node
		self.size += 1

	def searchNode(self,value):
		"""Searching Node in LinkedList (Nodes)"""
		currentNode = self.head
		nodeId = 1
		results = []
		while currentNode:
			if currentNode.hasValue(value):
				results.append(str(nodeId))
			currentNode = currentNode.nextNode
			nodeId += 1
		return results

	def updateNode(self,position,value):
		"""Update Node in LinkedList (Nodes)"""
		currentNode = self.head
		nodeId = 1
		while currentNode:
			if nodeId == position :
				currentNode.data = value
			currentNode = currentNode.nextNode
			nodeId += 1

	def insertNode(self,position,node):
		"""Insert node at a Specific Position"""
		if not isinstance(node,Node):
			node = Node(node)
		currentNode = self.head
		nodeId = 1
		while currentNode:
			if nodeId+1 == position :
				newNode = node
				newNode.nextNode = currentNode.nextNode
				currentNode.nextNode = newNode
				self.size += 1
			currentNode = currentNode.nextNode
			nodeId += 1

	def getSize(self):
		"""Return Size of Nodes"""
		return self.size

	def deleteNode(self,position):
		"""Delete Node in LinkedList (Nodes)"""
		if position == 1:
			self.head = self.head.nextNode
			self.head.nextNode
			return True
		currentNode = self.head
		nodeId = 1
		deleted = False
		while currentNode:
			if nodeId == position :
				currentNode.nextNode = currentNode.nextNode.nextNode
				self.size -= 1
				deleted = True
			currentNode = currentNode.nextNode
			nodeId += 1
		return deleted

	def displayNodes(self,invert=False):
		"""Display all LinkedList (Nodes)"""
		currentNode = self.head
		result = []
		while currentNode:
			result.append(currentNode.data)
			currentNode = currentNode.nextNode
		if invert:
			result.reverse()
			return result
		return result
# Part 1
print("[+] Create Nodes")

nodes = Nodes()
for node in ['2','6','7','8','1']:
	nodes.addNode(node)
print(', '.join(nodes.displayNodes()))

# Part 2
print("\n[+] Insert Node at 3rd position having value 9")
nodes.insertNode(3,'9')
print(', '.join(nodes.displayNodes()))

# Part 3
print("\n[+] Search Nodes having value 9 and 12")
for value in ['9','12']:
	foundNodes = nodes.searchNode(value)
	if foundNodes:
		print(f"[+] Nodes having value {value} are:",foundNodes)
	else:
		print(f"[-] No Node found having value {value}")

# Part 4
print("\n[+] Delete 3rd Node and display all Values")
nodes.deleteNode(3)
print("[+] Node Deleted")
print(', '.join(nodes.displayNodes()))
