CS526 HW6 - Problem 3
Zikai Zhou

I reuse MinHeap from hw6_question2.py for both halves. The lower heap stores negated values, so -lower.peek() gives the largest value in that half. The upper heap stores values as given, so upper.peek() gives its smallest value. I put the first sale in lower, then compare each new sale with the largest lower value to choose a heap. If the sizes get out of balance, I move the largest lower value or the smallest upper value across. This keeps all lower values at or below the upper values and gives lower either the same count or one more. For an odd count, I use the largest lower value. For an even count, I average the two roots after reversing the sign of the lower one. Reading the median takes O(1), each update takes O(log n), and empty input returns [].

Run in PowerShell from the homework folder.
Get-Content .\median_input1.txt | python .\hw6_question3.py

Keep hw6_question2.py and hw6_question3.py in the same folder.
