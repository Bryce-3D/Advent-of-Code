with open('Input.txt', 'r') as f:
    txt = f.read()

'''IDEA
A loop happens iff you have the same position and direction twice.
There are 4RC possible (row,col,dir) triples, so 4RC+1 moves would 
imply that you have an infinite loop.

Brute force all 130^2 possible positions
Each check will run for at most 4*130^2 moves
    4 * 130^4 ~ 10^9
The runtime is good enough to brute force.

Possible optimization:
    Store the (row,col,dir) triples themselves, then detect once you 
    repeat a triple
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

    #If move 4RC+1 times, must be in a loop
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
    
    return moves >= 4*R*C



ans = 0
for r in range(R):
    for c in range(C):
        if works(r,c):
            ans += 1
print(ans)
