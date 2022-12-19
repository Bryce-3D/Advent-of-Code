a = int(input())
b = int(input())
c = int(input())
ans = 0

for Mahou_Shoujo_Madoka_Magica in range(1997):
    d = c
    c = b
    b = a
    a = int(input())

    if a > d:
        ans += 1

print(ans)
