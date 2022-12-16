#Retrieving the info
f = open('AoC-2022-14-Input.txt', 'r')
inp = f.read().split('\n')
f.close()

#Eyeballing the input, 1000 should be a sufficient upper bound

#Processing the input
grid = [['.' for c in range(1001)] for r in range(1001)]
for path in inp:   #For each path of rocks
    path = path.split(' -> ')                    #Split the path into corners
    path = [v.split(',') for v in path]          #Split each vertex
    path = [[int(c) for c in v] for v in path]   #Convert each coord into ints
    path = [[v[1],v[0]] for v in path]           #Swap the order to put row first
    
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



#Starting coordinate is [0,500]
#We've fallen out of the grid when r reaches 1000
ans = 0
while True:
    r,c = 0,500   #Start from [0,500]
    while r < 1000:   #While not out of bounds
        if grid[r+1][c] == '.':       #Straight down
            r += 1
        elif grid[r+1][c-1] == '.':   #Down left
            r,c = r+1,c-1
        elif grid[r+1][c+1] == '.':   #Down right
            r,c = r+1,c+1
        else:                         #Stuck
            grid[r][c] = 'o'   #Mark the sand in the grid
            break              #Actually remember to break gdi

    if r < 1000:   #If we remember to exist
        ans += 1   #  One more grain gets stuck
    else:          #If we fall into the abyss
        break      #  Break

print(ans)



'''Recycling bin
#Parsing the input
#Split each path into vertices
inp = [path.split(' -> ') for path in inp]
#Split each vertex into its coordinates
inp = [[v.split(',') for v in path] for path in inp]
#Convert each coordinate into an integer
inp = [[[int(c) for c in v] for v in path] for path in inp]
#Swap each pair of coordinates to put the row first
inp = [[[]]]
'''
