
import sys
from math import gcd

n=int(sys.stdin.readline())
points=[]

for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    points.append((x,y))

answer=0

for i in range(n):
    x1,y1=points[i]
    directions={}

    for j in range(n):
        if i==j:
            continue

        x2,y2=points[j]
        dx=x2-x1
        dy=y2-y1

        g=gcd(abs(dx),abs(dy))
        dx//=g
        dy//=g

        direction=(dx,dy)

        if direction not in directions:
            directions[direction]=0

        directions[direction]+=1

    for direction in directions:
        dx,dy=direction
        perpendicular=(-dy,dx)
        answer+=directions[direction]*directions.get(perpendicular,0)

print("The number of right triangles is:",answer)
