import sys


def make_line(x1,y1,x2,y2):
    A=y2-y1
    B=x1-x2
    C=A*x1+B*y1

    return A,B,C


def lines_cross(line1,line2):
    A1,B1,C1=line1
    A2,B2,C2=line2

    det=A1*B2-A2*B1

    if det!=0:
        return True

    if A1*C2==A2*C1 and B1*C2==B2*C1:
        return True

    return False


n=int(sys.stdin.readline())

lines=[]

for i in range(n):
    parts=sys.stdin.readline().split()

    x1=int(parts[1])
    y1=int(parts[2])
    x2=int(parts[4])
    y2=int(parts[5])

    line=make_line(x1,y1,x2,y2)
    lines.append(line)


crossing=False

for i in range(len(lines)):
    for j in range(i+1,len(lines)):
        if lines_cross(lines[i],lines[j]):
            crossing=True
            break

    if crossing:
        break


if crossing:
    print("All Ghosts: were not eliminated")
else:
    print("All Ghosts: were eliminated")