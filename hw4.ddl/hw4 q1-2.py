#q1
#preorder traversal:ABEHFICDG
#breadth traversal:ABCFDEGHI
#postorder traversal:HEIFBCGDA

#q1
#inorder traversal:DGBEACHFI

#q2
import sys
n=int(sys.stdin.readline())
target=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
original=numbers.copy()
numbers.sort(reverse=True)
numbers.sort(reverse=True)


total=0
count=0
for number in numbers:
    if total>target:
        break
    total+=number
    count+=1
print("Input:",", ".join(map(str, original)),"Target:",target,"Answer:",count)
