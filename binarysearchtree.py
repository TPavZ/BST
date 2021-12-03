# insert_node and search_for_node logic
from node import Node

class Binarysearchtree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        else:
            if node.data < self.root.data:
                if self.root.left is None:
                    self.root.left = node.data     
                    # move down to next level                                      
                else:
                    if node.data < self.root.left:
                        self.root.left = node.data
                    else:
                        self.root.left.root.right = node.data 
                #else:
                    #self.root.left = node.data 
                    # put the node in on the left
                    
            if node.data > self.root.data:
                if self.root.right is None:
                    self.root.right = node.data
                else:
                    pass