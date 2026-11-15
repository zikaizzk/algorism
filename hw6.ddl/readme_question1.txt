CS526 HW6 - Problem 1
Zikai Zhou

I put the first sale from each nonempty register into a min-heap. Each
entry stores the time, register number, and position in that register's
list. The heap compares time first, then register number.

I take out the smallest entry, append its (time, register) pair, and
add the next sale from the same register if one remains. Since each
register is already sorted, its first remaining
sale is its earliest one. This also keeps at most one entry per register.
An empty list still counts as a register. Duplicate sales stay in the
result. I wrote the heap operations in Python.

For N sales and k registers, the merge takes O(k + N log(k+1)) time.
The heap holds at most k entries.

Run in PowerShell from the homework folder.
Get-Content .\merge_input1.txt | python .\hw6.py
