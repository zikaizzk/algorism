    I used 2D Array Traversal and Set
    My program checks whether a partially filled puzzle board is valid. First, it reads the board size, allowed symbols, and the board from standard input. Then, it checks each row and each column for duplicate symbols using a set. Empty cells represented by "." are skipped. Any non-empty symbol that is not in the allowed symbol list makes the board invalid. Next, the program divides the board into square sub-boards of size sqrt(n) by sqrt(n). It checks each sub-board for duplicate symbols using a new set.
     If any rule is violated, the board is invalid. Otherwise, it is valid.
     Time Complexity: O(n²), Extra Space Complexity: O(n), excluding the input board.

How to Run:
Get-Content .\puzzle_game_input1.txt | python .\puzzle_game.py
Replace the input filename with puzzle_game_input2.txt, puzzle_game_input3.txt, or puzzle_game_input4.txt to run the other tests.

Results:
Input 1: The board is valid
Input 2: The board is invalid
Input 3: The board is valid
Input 4: The board is invalid