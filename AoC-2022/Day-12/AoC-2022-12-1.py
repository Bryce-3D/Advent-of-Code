#Retrieving the info
f = open('AoC-2022-12-Input.txt', 'r')
inp = f.read().split('\n')
f.close()

#Number of rows and cols in the input
R = len(inp)
C = len(inp[0])
#The 4 directions
dirs = [[0,1],[0,-1],[1,0],[-1,0]]



#Set up the grid. Row and column numbers are both 
#0-indexed, and (0,0) is the top left corner
grid = [[0 for c in range(C)] for r in range(R)]
S = [-1,-1]   #Starting coord
E = [-1,-1]   #Ending coord
for r in range(R):
    for c in range(C):
        if inp[r][c] == 'S':
            grid[r][c] = 0
            S = [r,c]
        elif inp[r][c] == 'E':
            grid[r][c] = 25
            E = [r,c]
        else:
            grid[r][c] = ord(inp[r][c]) - ord('a')



#Perform the BFS
BFS = [S]
#dist[r][c] = dist from S to (r,c)
#Set to -1 for unvisited coordinates
dist = [[-1 for c in range(C)] for r in range(R)]
dist[S[0]][S[1]] = 0   #Initialize the start

#While there are unprocessed nodes in the BFS "queue"
i = 0
while i < len(BFS):
    #Currently looking at coordinates (r,c)
    r = BFS[i][0]
    c = BFS[i][1]

    #Check each of the (at most) 4 neighbors of (r,c)
    for dir in dirs:
        #Currently looking at the neighbor (r0,c0)
        r0 = r + dir[0]
        c0 = c + dir[1]

        #If not a valid coordinate, skip
        if not (0 <= r0 < R and 0 <= c0 < C):
            continue
        #If already visited, skip
        if dist[r0][c0] != -1:
            continue
        #If unreachable, skip
        if grid[r0][c0] - grid[r][c] > 1:
            continue

        #If neighbor is valid, unvisited, and reachable
        dist[r0][c0] = dist[r][c] + 1   #Update its dist
        BFS.append([r0,c0])             #Add (r0,c0) into the BFS

    i += 1   #Go to the next coordinate in the BFS

#Get the ans
print(dist[E[0]][E[1]])
