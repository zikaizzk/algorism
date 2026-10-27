   I used a loop to check each possible 3-day window and the input contains the snowfall totals. The algorism name is Sliding Window.
For the first 3 days, The total amount of snowfall is A[2]. For the test of the windows, I subtracted the cumulative snowfall of the day before the window starts from the cumulative snowfall of the last day of the window.
    About how to decide yse or no. I compare twice the three-day snowfall with the total snowfall to check whether it is strictly more than half.
    The time complexity is O(n). Extra space complexity is O(n).
    I used "Get-Content .\snowfall_input1.txt | python .\snowfall.py" to run the py text. every input runs one time.
    I compare twice the three-day snowfall with the total snowfall to check whether it is strictly more than half. The test results are:Input 1: YES, Input 2: NO, Input 3: NO, Input 4: YES, Input 5: YES