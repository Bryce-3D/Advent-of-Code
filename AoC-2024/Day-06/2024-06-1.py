with open('Input.txt', 'r') as f:
    txt = f.read()

'''
Problem seems to imply that the guard will leave and not get stuck in 
a loop, so can just brute force (worst case 4*grid size)
'''

M = [row for row in txt.split('\n')]
R,C = len(M),len(M[0])

seen = [[0 for c in range(C)] for r in range(R)]

#Find the start pos
for r in range(R):
    for c in range(C):
        if M[r][c] == '^':
            r0,c0 = r,c
r,c = r0,c0

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
