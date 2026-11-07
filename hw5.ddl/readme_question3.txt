 Problem 3

Algorithm
I used Dynamic Programming and Fenwick Trees to find the longest alternating increasing sequence from arrays A and B.
The sequence must have increasing values, alternate between A and B, and follow increasing original positions.
I used two DP states:
DA[i] is the longest valid sequence ending at A[i].
DB[i] is the longest valid sequence ending at B[i].

For each element, I look for the longest previous sequence from the opposite array with a smaller value and an earlier position.
I used coordinate compression to convert values into ranks. Two Fenwick Trees help find the maximum sequence length efficiently.
Both values at the current position are calculated before updating the trees. This prevents using two elements from the same position.
This algorithm works because each new element extends the best valid previous sequence while following the alternating and increasing rules.
The final answer is the maximum sequence length found.

Complexity
Time: O(N log N)
Space: O(N)
N is the total number of elements in both arrays.

How to Run
```text
python .\hw5question3.py longest_seq1.txt
python .\hw5question3.py longest_seq2.txt
python .\hw5question3.py longest_seq3.txt
python .\hw5question3.py longest_seq4.txt
python .\hw5question3.py longest_seq5.txt
python .\hw5question3.py longest_seq6.txt
```

Test Results
Input 1: 4
Input 2: 7
Input 3: 10
Input 4: 39
Input 5: 192
Input 6: 1
