with open('Input.txt', 'r') as f:
    txt = f.read()

'''IDEA
130x130 grid
Just brute force
Try all possible spots
Works iff you reach a spot a spot 5 times
Estimate = 2x10^7 ops
'''

M = [row for row in txt.split('\n')]
R,C = len(M),len(M[0])

#Find the start pos
for r in range(R):
    for c in range(C):
        if M[r][c] == '^':
            sta_r,sta_c = r,c

def works(r0:int,c0:int) -> bool:
    if M[r0][c0] != '.':
        return False
    _M = [[M[r][c] for c in range(C)] for r in range(R)]
    _M[r0][c0] = '#'

    

    # for row in _M:
    #     print(row)
    # print('\n\n')

    #If loop 4RC+1 times, must be in a loop
    r,c = sta_r,sta_c
    moves = 0
    dir = 0
    while moves <= 4*R*C:
        #Guard exits
        if dir == 0 and r == 0:
            break
        if dir == 1 and c == C-1:
            break
        if dir == 2 and r == R-1:
            break
        if dir == 3 and c == 0:
            break
        #N
        if dir == 0:
            #Turn OR
            if _M[r-1][c] == '#':
                dir = 1
                continue
            #Move
            r -= 1
            moves += 1
        #E
        if dir == 1:
            #Turn OR
            if _M[r][c+1] == '#':
                dir = 2
                continue
            #Move
            c += 1
            moves += 1
        #S
        if dir == 2:
            #Turn OR
            if _M[r+1][c] == '#':
                dir = 3
                continue
            #Move
            r += 1
            moves += 1
        #W
        if dir == 3:
            #Turn OR
            if _M[r][c-1] == '#':
                dir = 0
                continue
            #Move
            c -= 1
            moves += 1

        # print(r,c)
    
    return moves >= 4*R*C


# works(6,3)
# exit(0)



ans = 0
for r in range(R):
    for c in range(C):
        if works(r,c):
            ans += 1
print(ans)
exit(0)

dir = 0   #N=0, E=1, S=2, W=3
while True:
    #Mark current cell as visited
    seen[r][c] = 1

    #Guard exits
    if dir == 0 and r == 0:
        break
    if dir == 1 and c == C-1:
        break
    if dir == 2 and r == R-1:
        break
    if dir == 3 and c == 0:
        break

    #N
    if dir == 0:
        #Turn OR
        if M[r-1][c] == '#':
            dir = 1
            continue
        #Move
        r -= 1
    #E
    if dir == 1:
        #Turn OR
        if M[r][c+1] == '#':
            dir = 2
            continue
        #Move
        c += 1
    #S
    if dir == 2:
        #Turn OR
        if M[r+1][c] == '#':
            dir = 3
            continue
        #Move
        r += 1
    #W
    if dir == 3:
        #Turn OR
        if M[r][c-1] == '#':
            dir = 0
            continue
        #Move
        c -= 1

ans = sum([sum(row) for row in seen])
print(ans)

