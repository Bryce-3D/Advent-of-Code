with open('Input.txt', 'r') as f:
    txt = f.read()

M = txt.split('\n')
R,C = len(M),len(M[0])

#poses[c] = list of positions of c
poses = {}
for r in range(R):
    for c in range(C):
        if M[r][c] == '.':
            continue
        char = M[r][c]
        if char not in poses:
            poses[char] = [[r,c]]
        else:
            poses[char].append([r,c])

hit = [[0 for c in range(C)] for r in range(R)]
for char in poses:
    pos = poses[char]
    for i in range(len(pos)):
        for j in range(i):
            #Extract the positions of the same chars
            r_0,c_0 = pos[i]
            r_1,c_1 = pos[j]
            #Get the reflections
            x_0,y_0 = 2*r_1-r_0,2*c_1-c_0
            x_1,y_1 = 2*r_0-r_1,2*c_0-c_1
            #Mark as hit if they lie in the grid
            if 0<=x_0<R and 0<=y_0<C:
                hit[x_0][y_0] = 1
            if 0<=x_1<R and 0<=y_1<C:
                hit[x_1][y_1] = 1

ans = sum([sum(i) for i in hit])
print(ans)
