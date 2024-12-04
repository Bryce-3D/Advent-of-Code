with open('Input.txt', 'r') as f:
    txt = f.read()

M = txt.split('\n')
R,C = len(M),len(M[0])

ans = 0
for r in range(1,R-1):
    for c in range(1,C-1):
        if M[r][c] != 'A':
            continue
        if sorted([M[r-1][c-1],M[r+1][c+1]]) != ['M','S']:
            continue
        if sorted([M[r-1][c+1],M[r+1][c-1]]) != ['M','S']:
            continue
        ans += 1

print(ans)
