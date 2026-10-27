import sys
n=int(sys.stdin.readline())
symbols=sys.stdin.readline().strip().split(",")
board=[]
for i in range(n):
    row=sys.stdin.readline().strip().split(",")
    board.append(row)
valid=True
for row in board:
    seen=set()
    for symbol in row:
        if symbol==".":
            continue
        if symbol not in symbols or symbol in seen:
            valid=False
            break
        seen.add(symbol)
for j in range(n):
    seen=set()
    for i in range(n):
        symbol=board[i][j]
        if symbol==".":
            continue
        if symbol not in symbols or symbol in seen:
            valid=False
            break
        seen.add(symbol)
from math import isqrt

size=isqrt(n)
for r in range(0,n,size):
    for c in range(0,n,size):
        seen=set()
        for i in range(r,r+size):
            for j in range(c,c+size):
                symbol=board[i][j]
                if symbol==".":
                    continue
                if symbol not in symbols or symbol in seen:
                    valid=False
                    break
                seen.add(symbol)
if valid:
    print("The board is valid")
else:
    print("The board is invalid")