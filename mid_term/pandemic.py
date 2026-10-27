import sys
n=int(sys.stdin.readline())
board=[[0]*n for i in range(n)]
for line in sys.stdin:
    if line.strip():
        r,c=map(int,line.split())
        board[r][c]=1
directions=[(-1,0),(1,0),(0,-1),(0,1)]
while True:
    new=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                continue
            count=0
            for dr,dc in directions:
                nr=i+dr
                nc=j+dc
                if 0<=nr<n and 0<=nc<n:
                    if board[nr][nc]==1:
                        count+=1
            if count>=2:
                new.append((i,j))
    if not new:
        break
    for i,j in new:
        board[i][j]=1
healthy=False
for row in board:
    if 0 in row:
        healthy=True
        break
if healthy:
    print("There are healthy counties left")
else:
    print("There are no healthy counties left")