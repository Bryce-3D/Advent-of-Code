'''IDEA
Just BFS?
'''

with open('Input.txt', 'r') as f:
    txt = f.read()
blocked = [
    [int(i) for i in row.split(',')]
    for row in txt.split('\n')
]

#Grid is visually flipped !!!

X,Y = 71,71

passable = [
    [True for x in range(X)]
    for y in range(Y)
]
for i in range(1024):
    x,y = blocked[i]
    passable[x][y] = False

dists = [
    [None for x in range(X)]
    for y in range(Y)
]
dists[0][0] = 0

drts = [
    [-1,0],
    [1,0],
    [0,-1],
    [0,1],
]

BFS = [[0,0]]
ind = 0
while ind < len(BFS):
    x0,y0 = BFS[ind]   #Get next node

    for drt in drts:
        x,y = x0+drt[0],y0+drt[1]
        #Check if inside the grid
        if x < 0 or X <= x:
            continue
        if y < 0 or Y <= y:
            continue
        #Check if passable
        if not passable[x][y]:
            continue
        #Check if already in BFS queue
        if dists[x][y] != None:
            continue
        
        #Record dist and toss into BFS queue
        dists[x][y] = dists[x0][y0] + 1
        BFS.append([x,y])
    
    ind += 1

print(dists[-1][-1])

def reachable(passable:list[list[bool]]) -> bool:
    drts = [
        [-1,0],
        [1,0],
        [0,-1],
        [0,1],
    ]
    X,Y = len(passable),len(passable[0])
    seen = [
        [False for x in range(X)]
        for y in range(Y)
    ]
    BFS = [[0,0]]
    seen[0][0] = True
    ind = 0

    while ind < len(BFS):
        x0,y0 = BFS[ind]   #Get next node

        for drt in drts:
            x,y = x0+drt[0],y0+drt[1]
            #Check if inside the grid
            if x < 0 or X <= x:
                continue
            if y < 0 or Y <= y:
                continue
            #Check if passable
            if not passable[x][y]:
                continue
            #Check if already in BFS queue
            if seen[x][y]:
                continue
            
            #Record as seen and toss into BFS queue
            seen[x][y] = True
            BFS.append([x,y])
        
        ind += 1
    
    return seen[-1][-1]

passable = [
    [True for x in range(X)]
    for y in range(Y)
]
for i in range(3046):
    x,y = blocked[i]
    passable[x][y] = False

print(reachable(passable))
print(blocked[3045])

for i in range(3045,3060):
    passable = [
        [True for x in range(X)]
        for y in range(Y)
    ]
    for j in range(i):
        x,y = blocked[j]
        passable[x][y] = False
    
    if not reachable(passable):
        print(blocked[i])

#3000 can
#3250 cannot
#3125 cannot
#3060 cannot
#3030 can
#3045 can
#3050 cannot
#3048 cannot
#3046 cannot
print(blocked[3045])

#Not 43,61
