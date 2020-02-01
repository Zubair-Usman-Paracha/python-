
class Node:
    
    def __init__(self, data):
        self.item = data
        self.nref = None
        
class LinkedList:
    
    def __init__(self):
        self.node = None

    def insert_after_item(self, x, data) :
         if self.node is None:
            print("The given List is empty")
            return
         else:
            n = self.node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref = new_node

    def delete_element_by_value(self, x):
        if self.node is None:
            print("The list has no element to delete")
            return 
        if self.node.nref is None:
            if self.node.item == x:
                self.node = None
            else:
                print("Item not found")
            return 

        if self.node.item == x:
            self.node = self.start_node.nref
            self.node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

"""
new_linked_list = DoublyLinkedList()
new_linked_list.insert_in_emptylist(50)
new_linked_list.traverse_list()
"""
class Node:
    
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.start_node = None

    def insert_after_item(self, x, data) :
         if self.start_node is None:
            print("List is empty")
            return
         else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p
        
new_linked_list = DoublyLinkedList()
new_linked_list.insert_after_item(5, 15)
new_linked_list.delete_element_by_value(65)
new_linked_list.reverse_linked_list()
new_linked_list.insert_in_emptylist(1)
new_linked_list.traverse_list()











        




