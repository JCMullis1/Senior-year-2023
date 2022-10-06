class Node:
    def __init__(self, data):
        self.visited = False
        self.explored = False
        self.prev = None
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data

        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def BFS(self):
        pass

    def DFS(self):
        pass

    def binary_search(self):
        pass


root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')
