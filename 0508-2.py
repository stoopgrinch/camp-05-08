N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = ""

for i in range(N):
    if A[i] == B[i]:
        x += str(i + 1) 
        x += " "

if not x:
    print (0)

print(x)
