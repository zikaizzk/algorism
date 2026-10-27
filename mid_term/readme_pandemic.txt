    I used a 2D array and simulation to solve this problem.
    First, I created an NxN board. I used 0 to represent a healthy county and 1 to represent an infected county.
    For each day, I checked every healthy county and counted its infected neighbors. Only the 4 directions  were considered.
    For instance, If a healthy county had at least two infected neighbors, I added its position to a list called new. After checking the whole board, I updated all the counties in new at the same time. I repeated this process until no new counties became infected. Finally, I checked whether there were any healthy counties left and printed the required result.
    The time complexity is O(n^4) in the worst case, and the extra space complexity is O(n^2).

I used this commands to run my program in terminall:
Get-Content .\pandemic_input1.txt | python .\pandemic.py
Get-Content .\pandemic_input2.txt | python .\pandemic.py

test results:
Input 1: There are healthy counties left
Input 2: There are no healthy counties left