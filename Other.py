 def __init__(self,data):
        self.root = Node(data)
                
    def insert_node(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        if self.root is not None:
            if node.data < self.root.data:
                if self.root.left is not None: # circle back somehow
                    new_node = node.data
                    self.left = new_node
                    
                    
                    # move down to next level
                else:
                    self.root.left = node.data 
                    
                    # put the node in on the left
            if node.data > self.root.data:
                if self.root.right is not None:
                    self.root.right = node.data
                else:
                    self.root.right = node.data
    
    def insert_node(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        if self.root is not None:
            if node.data < self.root.data:
                if self.root.left:
                    # move down to next level
                    pass
                else:
                    # put the node in on the left