with open('Input.txt', 'r') as f:
    txt = f.read()

XMAS = 'XMAS'

M = txt.split('\n')
R,C = len(M),len(M[0])

ans = 0
for r in range(R):
    for c in range(C):
        #N
        if r >= 3:
            w = M[r][c] + M[r-1][c] + M[r-2][c] + M[r-3][c]
            if w == XMAS:
                ans += 1
        #NW
        if r >= 3 and c >= 3:
            w = M[r][c] + M[r-1][c-1] + M[r-2][c-2] + M[r-3][c-3]
            if w == XMAS:
                ans += 1
        #W
        if c >= 3:
            w = M[r][c] + M[r][c-1] + M[r][c-2] + M[r][c-3]
            if w == XMAS:
                ans += 1
        #SW
        if r <= R-4 and c >= 3:
            w = M[r][c] + M[r+1][c-1] + M[r+2][c-2] + M[r+3][c-3]
            if w == XMAS:
                ans += 1
        #S
        if r <= R-4:
            w = M[r][c] + M[r+1][c] + M[r+2][c] + M[r+3][c]
            if w == XMAS:
                ans += 1
        #SE
        if r <= R-4 and c <= C-4:
            w = M[r][c] + M[r+1][c+1] + M[r+2][c+2] + M[r+3][c+3]
            if w == XMAS:
                ans += 1
        #E
        if c <= C-4:
            w = M[r][c] + M[r][c+1] + M[r][c+2] + M[r][c+3]
            if w == XMAS:
                ans += 1
        #NE
        if r >= 3 and c <= C-4:
            w = M[r][c] + M[r-1][c+1] + M[r-2][c+2] + M[r-3][c+3]
            if w == XMAS:
                ans += 1

print(ans)
