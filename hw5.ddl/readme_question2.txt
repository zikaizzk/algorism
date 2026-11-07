Algorithm
I used Dynamic Programming to count the number of ways to split a Morse code sequence into vowels.
The vowel codes are A=.-, E=., I=.., O=---, and U=..-.
I used dp[i] to store the number of valid combinations for the first i symbols. Initially, dp[0]=1.
For each position, the program checks whether a vowel code matches the end of the current sequence. If it matches, the number of combinations from the previous position is added to dp[i].
The final answer is dp[n].
This method works because every valid combination must end with one of the five vowels. Dynamic Programming counts all possible combinations without repeating the same calculation.
Complexity
Time: O(n)
Space: O(n)

How to Run
python .\hw5question2.py vowel_input1.txt
python .\hw5question2.py vowel_input2.txt
python .\hw5question2.py vowel_input3.txt
python .\hw5question2.py vowel_input4.txt

Test Results
Input 1: 6
Input 2: 8
Input 3: 0
Input 4: 193050000

