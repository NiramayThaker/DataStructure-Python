class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left == None:
                self.left = BinarySearchTreeNode(data)
                return 
            self.left.add_child(data)
        
        if data > self.data:
            if self.right == None:
                self.right = BinarySearchTreeNode(data)
                return
            self.right.add_child(data)

    def InOrderTraversal(self):
        elements = []
        # Adding left node
        if self.left:
            elements += self.left.InOrderTraversal()

        # Adding root node (of main or sub tree)
        elements.append(self.data)
        
        #Adding right node
        if self.right:
            elements += self.right.InOrderTraversal()
        
        return elements

    def PreOrderTraversal(self):
        elements = []

        # Adding root node (of main or sub tree)
        elements.append(self.data)

        # Adding left node
        if self.left:
            elements += self.left.PreOrderTraversal()

        # Adding right node
        if self.right:
            elements += self.right.PreOrderTraversal()
        
        return elements
    
    def PostOrderTraversal(self):
        elements = []

        #Adding left node
        if self.left:
            elements += self.left.PostOrderTraversal()
        
        # Adding right node
        if self.right:
            elements += self.right.PostOrderTraversal()
        
        # Adding root node (of main or sub tree)
        elements.append(self.data)
    
        return elements

def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = buildTree(numbers)
    print(numbers_tree.PreOrderTraversal())
    print(numbers_tree.InOrderTraversal())
    print(numbers_tree.PostOrderTraversal())
