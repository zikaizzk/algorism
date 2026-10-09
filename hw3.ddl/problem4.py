import sys

def intersect(a,b):
    x1,y1,x2,y2=a
    x3,y3,x4,y4=b

    dx1=x2-x1
    dy1=y2-y1
    dx2=x4-x3
    dy2=y4-y3

    cross=dx1*dy2-dy1*dx2

    if cross!=0:
        return True

    if (x3-x1)*dy1-(y3-y1)*dx1==0:
        return True

    return False


def check_lines(lines):
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            if intersect(lines[i],lines[j]):
                return False
    return True


n=int(sys.stdin.readline())
lines=[]

for i in range(n):
    parts=list(map(float,sys.stdin.readline().split()))
    lines.append(parts)

if check_lines(lines):
    print("All Ghosts: were eliminated")
else:
    print("All Ghosts: were not eliminated")