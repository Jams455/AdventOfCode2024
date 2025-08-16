class Node:
    def __init__(self, value):
        self.value = value
        self.lower = None
        self.higher = None

    def Add_Value(self, value):
        if not self.value:
            self.value = value
        elif value > self.value:
            if not self.higher:
                self.higher = Node(value)
            else:
                self.higher.Add_Value(value)
        elif value < self.value:
            if not self.lower:
                self.lower = Node(value)
            else:
                self.lower.Add_Value(value)
        else:
            print("[-] ERROR: Adding same value twice")
            exit()
    
    def Search(self, value):
        if value == self.value:
            return True
        elif not self.value:
            return False
        elif value > self.value and self.higher:
            return self.higher.Search(value)
        elif value < self.value and self.lower:
            return self.lower.Search(value)
        else:
            return False
    
class BinarySearchTree(Node):
    def __init__(self):
        super().__init__(value=None)
    
    def Fill_Tree(self, values):
        for value in values:
            self.Add_Value(value)
