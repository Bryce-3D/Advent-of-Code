#Retrieving the info
f = open('AoC-2022-08-Input.txt', 'r')
tree = f.read().split('\n')
f.close()

#Convert the forest to ints and get the size
tree = [[int(h) for h in row] for row in tree]
R = len(tree)
C = len(tree[0])

#visible[r][c] = True iff trees[r][c] is visible
visible = [[False for c in range(C)] for r in range(R)]

#For each row
for r in range(R):
    #Check from the LEFT SIDE RIGHT SIDE HA O MUKIDASHITE PA PA PA
    M = -1   #Current max of row r from the left
    for c in range(C):
        if tree[r][c] > M:
            visible[r][c] = True
            M = tree[r][c]
    
    #Check from the right
    M = -1   #Current max of row r from the right
    for c in range(C-1,-1,-1):
        if tree[r][c] > M:
            visible[r][c] = True
            M = tree[r][c]

#For each col
for c in range(C):
    #Check from the top
    M = -1   #Current max of col c from the top
    for r in range(R):
        if tree[r][c] > M:
            visible[r][c] = True
            M = tree[r][c]
    
    #Check from the bottom
    M = -1   #Current max of col c from the bot
    for r in range(R-1,-1,-1):
        if tree[r][c] > M:
            visible[r][c] = True
            M = tree[r][c]

#Count the total number of visible trees
ans = 0
for r in range(R):
    for c in range(C):
        if visible[r][c]:
            ans += 1
print(ans)
