with open('Input.txt', 'r') as f:
    txt = f.read()

def solve(s,l) -> int:
    possible = [[l[0]]]
    for ind in range(1,len(l)):
        n = l[ind]
        prev = possible[-1]
        next = []
        for k in prev:
            if k+n <= s:
                next.append(k+n)
            if k*n <= s:
                next.append(k*n)
        possible.append(next)
    if s in possible[-1]:
        return s
    else:
        return 0

ans = 0
for line in txt.split('\n'):
    s,a = line.split(':')
    s = int(s)
    a = [int(i) for i in a.split()]
    ans += solve(s,a)

print(ans)

