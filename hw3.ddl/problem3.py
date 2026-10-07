class ArrayStack:
    def __init__(self):
        self.data=[]

    def push(self,value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data)==0

    def print_stack(self):
        print(", ".join(str(value) for value in self.data))


class SinglyNode:
    def __init__(self,value):
        self.value=value
        self.next=None


class SinglyStack:
    def __init__(self):
        self.head=None

    def push(self,value):
        new_node=SinglyNode(value)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        if self.is_empty():
            return None

        value=self.head.value
        self.head=self.head.next
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def is_empty(self):
        return self.head is None

    def print_stack(self):
        self.print_helper(self.head)

    def print_helper(self,node):
        if node is None:
            print()
            return

        self.print_helper_value(node)

    def print_helper_value(self,node):
        if node.next is not None:
            self.print_helper_value(node.next)
            print(", ",end="")
        print(node.value,end="")

        if node==self.head:
            print()


class DoublyNode:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None


class DoublyStack:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,value):
        new_node=DoublyNode(value)

        if self.tail is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node

    def pop(self):
        if self.is_empty():
            return None

        value=self.tail.value

        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None

        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.tail.value

    def is_empty(self):
        return self.tail is None

    def print_stack(self):
        self.print_helper(self.head)

    def print_helper(self,node):
        if node is None:
            print()
            return

        print(node.value,end="")

        if node.next is not None:
            print(", ",end="")
            self.print_helper(node.next)
        else:
            print()


def insert_bottom(stack,value):
    if stack.is_empty():
        stack.push(value)
        return

    top=stack.pop()

    insert_bottom(stack,value)

    stack.push(top)


def reverse_stack(stack):
    if stack.is_empty():
        return

    top=stack.pop()

    reverse_stack(stack)

    insert_bottom(stack,top)


def fill_stack(stack,value=1):
    if value>10:
        return

    stack.push(value)
    fill_stack(stack,value+1)


def test_stack(name,stack):
    fill_stack(stack)

    print(name)
    print("Before: ",end="")
    stack.print_stack()

    reverse_stack(stack)

    print("After: ",end="")
    stack.print_stack()


array_stack=ArrayStack()
singly_stack=SinglyStack()
doubly_stack=DoublyStack()

test_stack("Array Stack",array_stack)
test_stack("Singly Linked List Stack",singly_stack)
test_stack("Doubly Linked List Stack",doubly_stack)