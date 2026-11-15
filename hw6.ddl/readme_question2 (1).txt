CS526 HW6 - Problem 2
Zikai Zhou

I built the min-heap as a complete binary tree. Each node stores a value and links to its parent and children. I find a position using its binary digits after the first 1, going left for 0 and right for 1. Insert fills the next spot and moves a value up only when it is smaller than its parent. Peek reads the root, and extract_min removes it by moving the last value to the root and sifting it down. Both raise IndexError on an empty heap. Delete finds and removes one copy, fills the gap with the last value, and sifts as needed. It returns False if the value is missing and True if it removes a copy. Build sifts down from the bottom up, and heap_sort extracts values from a copy. The node count supports len and is_empty. The program prints the tree after each insert, using slashes to show the links. Insert and extract_min take O(log n), delete and build take O(n), and heap_sort takes O(n log n).

Run in PowerShell from the homework folder.
Get-Content .\heap_input1.txt | python .\hw6_question2.py
