N = int(input())
a = [int(input()) for _ in range(N)]

x = 0
y = 0

for i in range(N):
    if i % 4 == 0:
        y += a[i]
    elif i % 4 == 1:
        x += a[i]
    elif i % 4 == 2:
        y -= a[i]
    else:
        x -= a[i]

print(x, y)
