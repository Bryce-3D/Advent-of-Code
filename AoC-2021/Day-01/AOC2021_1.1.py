a = int(input())
ans = 0
for i in range(1999):
    b = a
    a = int(input())
    if a > b:
        ans += 1
print(ans)
