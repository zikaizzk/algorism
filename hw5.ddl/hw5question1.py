import random

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BST:
    def __init__(self):
        self.root=None
    def AddNode(self,value):
        if self.root is None:
            self.root=Node(value)
            return
        current=self.root
        while True:
            if value<current.value:
                if current.left is None:
                    current.left=Node(value)
                    return
                current=current.left
            elif value>current.value:
                if current.right is None:
                    current.right=Node(value)
                    return
                current=current.right
            else:
                return
    def FindNode(self,value):
        current=self.root
        while current is not None:
            if value==current.value:
                return True
            elif value<current.value:
                current=current.left
            else:
                current=current.right
        return False
    def DeleteNode(self,value):
        self.root=self._delete(self.root,value)
    def _delete(self,node,value):
        if node is None:
            return None
        if value<node.value:
            node.left=self._delete(node.left,value)
        elif value>node.value:
            node.right=self._delete(node.right,value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor=node.right
            while successor.left is not None:
                successor=successor.left
            node.value=successor.value
            node.right=self._delete(node.right,successor.value)
        return node

    def PrintTree(self):
        if self.root is None:
            print("Empty tree")
            return
        self._print(self.root,0,"Root: ")

    def _print(self,node,level,label):
        if node is None:
            return
        print("    "*level+label+str(node.value))
        self._print(node.left,level+1,"L: ")
        self._print(node.right,level+1,"R: ")

def main():
    n=random.randint(5,50)
    numbers=random.sample(range(1,1001),n)
    print("Input size:",n)
    print("Input set:",numbers)
    tree=BST()
    for value in numbers:
        tree.AddNode(value)
    print("\nInitial tree:")
    tree.PrintTree()
    added=random.randint(1,1000)
    while tree.FindNode(added):
        added=random.randint(1,1000)
    print("\nAddNode:",added)
    tree.AddNode(added)
    tree.PrintTree()
    found=random.choice(numbers)
    print("\nFindNode:",found)
    if tree.FindNode(found):
        print("Node found")
    else:
        print("Node not found")
    missing=random.randint(1,1000)
    while tree.FindNode(missing):
        missing=random.randint(1,1000)

    print("\nFindNode:",missing)
    if tree.FindNode(missing):
        print("Node found")
    else:
        print("Node not found")
    print("\nDeleteNode:",added)
    tree.DeleteNode(added)
    tree.PrintTree()

    deleted=numbers[0]
    print("\nDeleteNode:",deleted)
    tree.DeleteNode(deleted)
    tree.PrintTree()
if __name__=="__main__":
    main()