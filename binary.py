class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insertnode(self,data):
        if data<self.data:
            if self.left is not None:
                 return self.left.insertnode(data)
            else:
                self.left=Node(data)
        else:
            if self.right is not None:
                return self.right.insertnode(data)
            else:
                self.right=Node(data)
    def findnode(self,data):
        if data==self.data:
            return True
        elif data<self.data and self.left:
            return self.left.findnode(data)
        elif data>self.data and self.right:
            return self.right.findnode(data)
        return False
    def preorder(self,List):
        List.append(self.data)
        if self.left :
            self.left.preorder(List)
        if self.right:
            self.right.preorder(List)
        return List
    def postorder(self,List):
        if self.left is not None:
            self.left.postorder(List)
        if self.right is not None:
            self.right.postorder(List)
        List.append(self.data)
        return List
    def inorder(self,List):
        if self.left is not None:
            self.left.inorder(List) 
        List.append(self.data)
        if self.right is not None:
            self.right.inorder(List)
        return List

class binarysearchtree:
    def createtree(self):
        self.root=None
    def insertnode(self,data):
        if self.root is not None:
            self.root.insertnode(data)
        else:
            self.root=Node(data)
    def findnode(self,data):
        return self.root.findnode(data)
    def preorder(self):
        return self.root.preorder([])
    def postorder(self):
        return self.root.postorder([])
    def inorder(self):
        return self.root.inorder([])
bst = binarysearchtree()
bst.createtree()
bst.insertnode(100)
bst.insertnode(50)
bst.insertnode(200)
bst.insertnode(300)
bst.insertnode(20)
bst.insertnode(150)
bst.insertnode(70)
bst.insertnode(180)
bst.insertnode(120)
bst.insertnode(30)
print(bst.findnode(6))
print("preorder : ",bst.preorder())
print("inorder : ",bst.inorder())
print("postorder : ",bst.postorder())
