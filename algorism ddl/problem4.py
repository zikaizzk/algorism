class Node:
    def __init__(self, value):
        self.value=value
        self.prev=None
        self.next=None


class SortedDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0


    def add(self, value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.size+=1
            return

        if value<=self.head.value:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.size+=1
            return

        current=self.head

        while current.next is not None and current.next.value<value:
            current=current.next

        new_node.next=current.next
        new_node.prev=current

        if current.next is not None:
            current.next.prev=new_node
        else:
            self.tail=new_node

        current.next=new_node
        self.size+=1


    def delete(self, value):
        current=self.head

        while current is not None and current.value<value:
            current=current.next

        if current is None or current.value!=value:
            return False

        if current.prev is None:
            self.head=current.next
        else:
            current.prev.next=current.next

        if current.next is None:
            self.tail=current.prev
        else:
            current.next.prev=current.prev

        self.size-=1
        return True


    def exists(self, value):
        return self.exists_helper(self.head, value)


    def exists_helper(self, current, value):
        if current is None:
            return False

        if current.value==value:
            return True

        if current.value>value:
            return False

        return self.exists_helper(current.next, value)


    def print_list(self):
        if self.head is None:
            print("(empty)")
            return

        self.print_helper(self.head)
        print()


    def print_helper(self, current):
        if current is None:
            return

        print(current.value, end="")

        if current.next is not None:
            print(" <-> ", end="")

        self.print_helper(current.next)


    def total(self):
        return self.total_helper(self.head)


    def total_helper(self, current):
        if current is None:
            return 0

        return current.value+self.total_helper(current.next)


    def count(self, value):
        return self.count_helper(self.head, value)


    def count_helper(self, current, value):
        if current is None:
            return 0

        if current.value>value:
            return 0

        if current.value==value:
            return 1+self.count_helper(current.next, value)

        return self.count_helper(current.next, value)


    def sum_middle_three(self):
        if self.size<3:
            raise ValueError("List must have at least 3 nodes")

        middle=self.size//2

        if self.size%2==0:
            middle=middle-1

        current=self.head

        for i in range(middle-1):
            current=current.next

        return current.value+current.next.value+current.next.next.value


    def median(self):
        if self.size==0:
            raise ValueError("List is empty")

        middle=self.size//2
        current=self.head

        if self.size%2==1:
            for i in range(middle):
                current=current.next

            return current.value

        else:
            for i in range(middle-1):
                current=current.next

            return (current.value+current.next.value)/2


my_list=SortedDoublyLinkedList()

my_list.add(10)
my_list.add(4)
my_list.add(29)
my_list.add(8)
my_list.add(2)
my_list.add(15)
my_list.add(41)

print("List:")
my_list.print_list()

print("Total:", my_list.total())
print("Sum middle three:", my_list.sum_middle_three())
print("Median:", my_list.median())

print("Delete 41:", my_list.delete(41))

print("List after deleting 41:")
my_list.print_list()

print("Total:", my_list.total())
print("Sum middle three:", my_list.sum_middle_three())
print("Median:", my_list.median())

my_list.add(8)

print("List after adding another 8:")
my_list.print_list()

print("Count of 8:", my_list.count(8))
print("Count of 5:", my_list.count(5))

print("Exists 15:", my_list.exists(15))
print("Exists 5:", my_list.exists(5))