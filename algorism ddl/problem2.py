class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.count +=1

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.count +=1

    def insert(self,index,value):
        if index<0 or index>self.count:
            raise IndexError
        if index==0:
            self.prepend(value)
            return
        if index==self.count:
            self.append(value)
            return
        current=self.head
        for i in range(index-1):
            current=current.next
        new_node=Node(value)
        new_node.next=current.next
        current.next=new_node
        self.count +=1

    def get(self,index):
        if index<0 or index>=self.count:
            raise IndexError
        current=self.head
        for i in range(index):
            current=current.next
        return current.value


    def find(self,value):
        current=self.head
        index=0
        while current is not None:
            if current.value==value:
                return index
            current=current.next
            index +=1
        return -1


    def __len__(self):
        return self.count

    def update(self,index,value):
        if index<0 or index>=self.count:
            raise IndexError
        current=self.head
        for i in range(index):
            current=current.next
        current.value=value


    def delete(self,value):
        current=self.head
        previous=None
        while current is not None:
            if current.value==value:
                if previous is None:
                    self.head=current.next
                else:
                    previous.next=current.next
                if current==self.tail:
                    self.tail=previous
                self.count -=1
                return True
            previous=current
            current=current.next
        return False


    def delete_at(self,index):
        if index<0 or index>=self.count:
            raise IndexError
        if index==0:
            value=self.head.value
            self.head=self.head.next
            if self.count==1:
                self.tail=None
            self.count -=1
            return value
        previous=self.head
        for i in range(index-1):
            previous=previous.next

        current=previous.next
        previous.next=current.next

        if current==self.tail:
            self.tail=previous

        self.count -=1
        return current.value


    def print_list(self):
        if self.head is None:
            print("(empty)")
            return

        current=self.head

        while current is not None:
            print(current.value,end="")
            if current.next is not None:
                print(" -> ",end="")
            current=current.next
        print()