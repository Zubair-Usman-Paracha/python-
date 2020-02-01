class Nodes:
    def __init__(self,data = None):
        self.data = data
        self.nextadd = None
        
node=Nodes()
n1 = Nodes(2)
n2 = Nodes(6)
n3 = Nodes(7)
n4 = Nodes(8)
n5 = Nodes(1)
n1.nextadd=n2
n2.nextadd=n3
n3.nextadd=n4
n4.nextadd=n5

thisvalue = n1

while thisvalue:
    print(thisvalue.data)
    thisvalue = thisvalue.nextadd

   

