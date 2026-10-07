Homework 2

Introduction

Problem 1, I answer the question
Problem 2, I created a singly linked list, which supports append, prepend, insert, get, find, update, delete, delete_at, and print_list.
Problem 3, I used recursion to calculate how to climb stairs.
Problem 4, I implemented a sorted doubly linked list. The list keeps the values in ascending order and supports operations.

Problem 1
tail pointer gives direct access to the last node.
It reduce the traverse time(O(1)) because if we do not have tail pointer,
 we need to traverse the entire list from the head to find 
 the last node when appending a new value(O(n)).



Problem 2
I use class to create node and SinglyLinkedList.
Each node stores a value and a pointer to the next node.
The linked keeps track of the head, tail, and number of nodes.
I use the tail pointer to add a new node to the end of the list for append,and prepand is add a new to the head.
For insert, I move through the list until I find the correct index and insert the new node.
For get, find, update, delete, and delete_at, I move through the linked list to find the required node.
The driver reads commands from standard input and performs the corresponding linked list operation.

Problem 3
I used recursion for the climbing stairs problem.
ways(n) = ways(n-1) + ways(n-2) + ways(n-3)


Problem 4
I used a doubly linked list where each node has a previous pointer and a next pointer.
When a new value is added, the program finds the correct position so the list stays sorted in ascending order.
The delete method changes both the previous and next pointers to remove a node.
I used recursive helper functions for exists, print_list, total, and count.
The median method find the middle value when the number of nodes is odd. When the number of nodes is even, it calculates the average of the two middle values.

Interesting

The most interesting thing during the process is I apply the basic knowledge of linkedlist to python environment. There are many senarios I need to consider,it is not only about the situation in the linkedlist, but also if the pointer is out of the list.The recursion is also very fun, I like it because it use most easy way to solve a giant problem.

