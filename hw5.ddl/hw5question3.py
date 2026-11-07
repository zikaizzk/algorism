import sys

def longest_sequence(A,B):
    values=sorted(set(A+B))
    ranks={value:i+1 for i,value in enumerate(values)}
    m=len(values)
    treeA=[0]*(m+1)
    treeB=[0]*(m+1)
    def query(tree,index):
        answer=0
        while index>0:
            answer=max(answer,tree[index])
            index-=index&-index
        return answer
    def update(tree,index,length):
        while index<=m:
            tree[index]=max(tree[index],length)
            index+=index&-index
    answer=0
    for i in range(max(len(A),len(B))):
        lengthA=0
        lengthB=0
        if i<len(A):
            rankA=ranks[A[i]]
            lengthA=query(treeB,rankA-1)+1
        if i<len(B):
            rankB=ranks[B[i]]
            lengthB=query(treeA,rankB-1)+1
        if i<len(A):
            update(treeA,rankA,lengthA)
        if i<len(B):
            update(treeB,rankB,lengthB)
        answer=max(answer,lengthA,lengthB)
    return answer

filename=sys.argv[1]
with open(filename,"r") as file:
    n=int(file.readline())
    m=int(file.readline())
    A=list(map(int,file.readline().split()))
    B=list(map(int,file.readline().split()))
answer=longest_sequence(A,B)
print("File Input:",filename)
print("Longest Sequence:",answer)