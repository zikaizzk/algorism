import sys
def find_substrings(word,start,end,result):
    if start>=len(word):
        return

    if end>len(word):
        find_substrings(word,start+1,start+2,result)
        return

    result.add(word[start:end])

    find_substrings(word,start,end+1,result)


word=sys.stdin.readline().strip()

result=set()

find_substrings(word,0,1,result)

for substring in sorted(result):
    print(substring)

print(len(result))