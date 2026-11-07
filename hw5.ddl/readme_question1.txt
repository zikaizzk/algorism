Algorithm
I used a Binary Search Tree (BST). Each node has a value, a left child, and a right child.
AddNode inserts a value into the correct position. FindNode searches for a value by moving left or right. DeleteNode handles three situations: a node with no children, one child, or two children. For two children, I replace the node's value with the smallest value in its right subtree.
PrintTree uses recursion to display the tree with indentation.
These operations follow the BST rule: smaller values are stored on the left and larger values on the right. This keeps the tree valid after insertion and deletion.
Complexity
AddNode, FindNode, DeleteNode: O(h) time.
PrintTree: O(n) traversal time.
Balanced BST: O(log n) height.
Worst-case unbalanced BST: O(n) height.
Here, n is the number of nodes and h is the tree height.

How to Run
python .\hw5.py
No input file is required.
Test Results
The program generates random values and demonstrates insertion, searching, deletion, and printing.
It tests both successful and unsuccessful searches. The added node and the original root are deleted, and the tree is printed after each change.
The output changes between runs because the values are randomly generated. Actual running screenshots are included with the submission.