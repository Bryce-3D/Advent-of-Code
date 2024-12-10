with open('Input.txt', 'r') as f:
    txt = f.read()

XMAS = 'XMAS'

M = txt.split('\n')
R,C = len(M),len(M[0])

dirs = [
    [-1, 0],   #N
    [-1,-1],   #NW
    [ 0,-1],   #W
    [ 1,-1],   #SW
    [ 1, 0],   #S
    [ 1, 1],   #SE
    [ 0, 1],   #E
    [-1, 1],   #NE
]

ans = 0
for r in range(R):
    for c in range(C):
        for dir in dirs:
            #Get the coordinates along the direction
            r1,c1 = r+1*dir[0],c+1*dir[1]
            r2,c2 = r+2*dir[0],c+2*dir[1]
            r3,c3 = r+3*dir[0],c+3*dir[1]
            #Check that it is inside the grid
            if min(r,r3) < 0 or max(r,r3) >= R:
                continue
            if min(c,c3) < 0 or max(c,c3) >= C:
                continue
            #Check if it spells 'XMAS'
            w = M[r][c]+M[r1][c1]+M[r2][c2]+M[r3][c3]
            if w == 'XMAS':
                ans += 1

print(ans)





#Recycling Bin ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # #N
        # if r >= 3:
        #     w = M[r][c] + M[r-1][c] + M[r-2][c] + M[r-3][c]
        #     if w == XMAS:
        #         ans += 1
        # #NW
        # if r >= 3 and c >= 3:
        #     w = M[r][c] + M[r-1][c-1] + M[r-2][c-2] + M[r-3][c-3]
        #     if w == XMAS:
        #         ans += 1
        # #W
        # if c >= 3:
        #     w = M[r][c] + M[r][c-1] + M[r][c-2] + M[r][c-3]
        #     if w == XMAS:
        #         ans += 1
        # #SW
        # if r <= R-4 and c >= 3:
        #     w = M[r][c] + M[r+1][c-1] + M[r+2][c-2] + M[r+3][c-3]
        #     if w == XMAS:
        #         ans += 1
        # #S
        # if r <= R-4:
        #     w = M[r][c] + M[r+1][c] + M[r+2][c] + M[r+3][c]
        #     if w == XMAS:
        #         ans += 1
        # #SE
        # if r <= R-4 and c <= C-4:
        #     w = M[r][c] + M[r+1][c+1] + M[r+2][c+2] + M[r+3][c+3]
        #     if w == XMAS:
        #         ans += 1
        # #E
        # if c <= C-4:
        #     w = M[r][c] + M[r][c+1] + M[r][c+2] + M[r][c+3]
        #     if w == XMAS:
        #         ans += 1
        # #NE
        # if r >= 3 and c <= C-4:
        #     w = M[r][c] + M[r-1][c+1] + M[r-2][c+2] + M[r-3][c+3]
        #     if w == XMAS:
        #         ans += 1