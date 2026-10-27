import sys
n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

total=A[-1]
answer="NO"
for i in range(n-2):
    if i==0:
        snow=A[i+2]
    else:
        snow=A[i+2]-A[i-1]
    if snow*2>total:
        answer="YES"
        break
print(" ".join(map(str,A)),"solution:",answer)