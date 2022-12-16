#For time tracking purposes
#Time taken: 1.3099830150604248s
import time
time_0 = time.time()

#Retrieving the info
f = open('AoC-2022-14-Input.txt', 'r')
inp = f.read().split('\n')
f.close()

'''
Sand could slide off quite far on the left and right ends.
Need to add extra space on both sides to account for this.
Negative indices let us teleport to the right end of an 
array, so we can just put the extra space for the left at 
the right end instead, making the right extension bigger.

R rows -> max overflow of an R by R right triangle at 
either side, so 2R extra columns at the end should be 
sufficient hopefully.
'''

#Processing the input
paths = []
for path in inp:   #For each path of rocks
    path = path.split(' -> ')                    #Split the path into corners
    path = [v.split(',') for v in path]          #Split each vertex
    path = [[int(c) for c in v] for v in path]   #Convert each coord into ints
    path = [[v[1],v[0]] for v in path]           #Swap the order to put row first
    paths.append(path)                           #Store in `paths`

#Get max row number
R = [[v[0] for v in path] for path in paths]   #Get row of each corner
R = [max(group) for group in R]                #Get max row number of each path
R = max(R) + 3                                 #Max row among max of each path + 3 (0-index it)
#Get max col number
C = [[v[1] for v in path] for path in paths]   #Get col of each corner
C = [max(group) for group in C]                #Get max col number of each path
C = max(C) + 2*R                               #Max col among max of each path + 2R

#Setting the grid
grid = [['.' for c in range(C)] for r in range(R)]
for path in paths:
    #Draw each segment onto the grid
    l = len(path)
    for i in range(l-1):
        #Get the endpoints
        v0 = path[i]
        v1 = path[i+1]
        if v0[0] == v1[0]:   #If horizontal
            r = v0[0]
            c_min = min(v0[1], v1[1])
            c_max = max(v0[1], v1[1])
            for c in range(c_min, c_max+1):
                grid[r][c] = '#'
        if v0[1] == v1[1]:   #If vertical
            c = v0[1]
            r_min = min(v0[0], v1[0])
            r_max = max(v0[0], v1[0])
            for r in range(r_min, r_max+1):
                grid[r][c] = '#'
#Bottom floor
for c in range(C):
    grid[-1][c] = '#'



#Starting coordinate is [0,500]
ans = 0
while grid[0][500] != 'o':   #While the source is not blocked
    ans += 1
    r,c = 0,500   #Start from [0,500]
    while True:   #While not stuck
        if grid[r+1][c] == '.':       #Straight down
            r += 1
        elif grid[r+1][c-1] == '.':   #Down left
            r,c = r+1,c-1
        elif grid[r+1][c+1] == '.':   #Down right
            r,c = r+1,c+1
        else:                         #Stuck
            grid[r][c] = 'o'   #Mark the sand in the grid
            break              #Stop falling

print(ans)



#For time tracking purposes
time_1 = time.time()
duration = time_1 - time_0
print(f'Time taken: {duration}s')
