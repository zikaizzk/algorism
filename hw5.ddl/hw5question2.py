import sys
filename=sys.argv[1]
with open(filename,"r") as file:
    n=int(file.readline())
    sequence=file.readline().strip()
vowels=[".-",".","..","---","..-"]
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    for code in vowels:
        length=len(code)
        if i>=length and sequence[i-length:i]==code:
            dp[i]+=dp[i-length]
print("File Input:",filename)
print("The Number of Vowel combinations is:",dp[n])