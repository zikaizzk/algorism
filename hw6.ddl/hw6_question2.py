import sys
from ast import literal_eval


class Node:
    def __init__(self,value,parent=None):
        self.value=value
        self.left=None
        self.right=None
        self.parent=parent


class MinHeap:
    def __init__(self):
        self.root=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def _node_at(self,position):
        node=self.root

        for bit in bin(position)[3:]:
            if bit=="0":
                node=node.left
            else:
                node=node.right

        return node

    def _sift_up(self,node):
        while node.parent is not None and node.value<node.parent.value:
            node.value,node.parent.value=node.parent.value,node.value
            node=node.parent

    def _sift_down(self,node):
        while node.left is not None:
            child=node.left

            if node.right is not None and node.right.value<child.value:
                child=node.right

            if child.value>=node.value:
                break

            node.value,child.value=child.value,node.value
            node=child

    def insert(self,value):
        position=self.size+1

        if position==1:
            self.root=Node(value)
        else:
            parent=self._node_at(position//2)
            node=Node(value,parent)

            if position%2==0:
                parent.left=node
            else:
                parent.right=node

            self._sift_up(node)

        self.size+=1

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty heap")

        return self.root.value

    def _detach_last(self,node):
        if node.parent.left is node:
            node.parent.left=None
        else:
            node.parent.right=None

        node.parent=None

    def extract_min(self):
        smallest=self.peek()

        if self.size==1:
            self.root=None
            self.size=0
            return smallest

        last=self._node_at(self.size)
        self.root.value=last.value
        self._detach_last(last)
        self.size-=1
        self._sift_down(self.root)

        return smallest

    def _find(self,node,value):
        if node is None:
            return None

        if node.value==value:
            return node

        found=self._find(node.left,value)

        if found is not None:
            return found

        return self._find(node.right,value)

    def delete(self,value):
        node=self._find(self.root,value)

        if node is None:
            return False

        if self.size==1:
            self.root=None
            self.size=0
            return True

        last=self._node_at(self.size)

        if node is last:
            self._detach_last(last)
            self.size-=1
            return True

        node.value=last.value
        self._detach_last(last)
        self.size-=1

        if node.parent is not None and node.value<node.parent.value:
            self._sift_up(node)
        else:
            self._sift_down(node)

        return True

    def _build_tree(self,values,position,parent):
        if position>len(values):
            return None

        node=Node(values[position-1],parent)
        node.left=self._build_tree(values,2*position,node)
        node.right=self._build_tree(values,2*position+1,node)
        self._sift_down(node)

        return node

    def build(self,values):
        self.root=self._build_tree(values,1,None)
        self.size=len(values)

    def _copy_tree(self,node,parent):
        if node is None:
            return None

        copied=Node(node.value,parent)
        copied.left=self._copy_tree(node.left,copied)
        copied.right=self._copy_tree(node.right,copied)

        return copied

    def heap_sort(self):
        copied=MinHeap()
        copied.root=self._copy_tree(self.root,None)
        copied.size=self.size
        result=[]

        while not copied.is_empty():
            result.append(copied.extract_min())

        return result

    def _max_width(self,node):
        if node is None:
            return 0

        return max(len(str(node.value)),self._max_width(node.left),self._max_width(node.right))

    def _values_at(self,node,depth,width):
        if node is None:
            return " "*width

        if depth==0:
            return str(node.value).center(width)

        half=width//2
        return self._values_at(node.left,depth-1,half)+self._values_at(node.right,depth-1,half)

    def _edges_at(self,node,depth,width):
        if node is None:
            return " "*width

        half=width//2

        if depth==0:
            left="/" if node.left is not None else ""
            right="\\" if node.right is not None else ""
            return left.center(half)+right.center(half)

        return self._edges_at(node.left,depth-1,half)+self._edges_at(node.right,depth-1,half)

    def print_heap(self):
        if self.is_empty():
            print("Empty heap")
            return

        levels=self.size.bit_length()
        cell=self._max_width(self.root)+2
        width=cell*(1<<(levels-1))

        for depth in range(levels):
            print(self._values_at(self.root,depth,width).rstrip())

            if depth<levels-1:
                print(self._edges_at(self.root,depth,width).rstrip())


def main():
    values=literal_eval(sys.stdin.read())
    heap=MinHeap()
    print("Input values:",values)

    for value in values:
        heap.insert(value)
        print("\nAfter insert("+str(value)+"):")
        heap.print_heap()


if __name__=="__main__":
    main()

