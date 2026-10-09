import sys

count=0

for line in sys.stdin:
    line=line.strip()
    line=line.replace(" ","")

    if line==line[::-1]:
        print(True)
        count+=1
    else:
        print(False)

print(count)