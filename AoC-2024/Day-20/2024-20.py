'''IDEA
Part 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is exactly one path.
From the sample and tracing the input, it seems that it 
literally is one path and no extra squares.

Obtain the path via BFS (or just finding the next adjacent 
road at each step)
dist = {coordinate:dist from start}

for coordinate on the road:
    check coords 2 manhattan dist away
    if is road and >=100 in front based on dist
        ans += 1

Part 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Just do the same thing but for all possible cheat 
durations from 1 to 20.
Well a cheat of duration 1 must stay on the track, 
so that one can be skipped.
'''

def get_sta(maze:list[str]) -> tuple[int,int]:
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                return (r,c)
    raise Exception('No start found in the maze')

def get_end(maze:list[str]) -> tuple[int,int]:
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'E':
                return (r,c)
    raise Exception('No end found in the maze')

def get_path(maze:list[str]) -> list[tuple[int,int]]:
    drts = [(-1,0),(1,0),(0,-1),(0,1)]
    R,C = len(maze),len(maze[0])
    ans = [get_sta(maze)]
    end = get_end(maze)
    while True:
        r0,c0 = ans[-1]   #Get last visited coordinate
        for drt in drts:
            r,c = r0+drt[0],c0+drt[1]   #Get neighbor
            #Check if the neighbor is in the grid
            if 0 > r or r >= R:
                continue
            if 0 > c or c >= C:
                continue
            #Check if the neighbor is passable
            if maze[r][c] == '#':
                continue
            #Check if this is backtracking
            if len(ans) > 1 and ans[-2] == (r,c):
                continue
            ans.append((r,c))
            break
        #Make sure that something was added
        if ans[-1] == (r0,c0):
            raise Exception('Dead end found')
        #Check if we're at the end
        if ans[-1] == end:
            return ans
        #Prevent infinite loop
        if len(ans) > R*C:
            raise Exception('Bug')

def get_mht_dist_away(coord:tuple[int,int], R:int, C:int, 
             d:int) -> list[tuple[int,int]]:
    '''
    Get a list of coordinates with a Manhattan Distance of 
    exactly d within an R by C grid
    '''
    ans = []
    r0,c0 = coord
    for i in range(d):
        #[N,W)
        r,c = r0-d+i,c0-i
        if 0 <= r < R and 0 <= c < C:
            ans.append((r,c))
        #[W,S)
        r,c = r0+i,c0-d+i
        if 0 <= r < R and 0 <= c < C:
            ans.append((r,c))
        #[S,E)
        r,c = r0+d-i,c0+i
        if 0 <= r < R and 0 <= c < C:
            ans.append((r,c))
        #[E,N)
        r,c = r0-i,c0+d-i
        if 0 <= r < R and 0 <= c < C:
            ans.append((r,c))
    return ans

def solve_1(maze:list[str], thresh:int) -> int:
    R,C = len(maze),len(maze[0])
    path = get_path(maze)
    ans = 0

    coord_to_dist = {}
    for i in range(len(path)):
        coord_to_dist[path[i]] = i

    for cheat_sta in path:
        d0 = coord_to_dist[cheat_sta]
        cheat_ends = get_mht_dist_away(cheat_sta,R,C,2)
        for cheat_end in cheat_ends:
            if cheat_end not in coord_to_dist:
                continue
            d1 = coord_to_dist[cheat_end]
            #Account a +2 for cheat duration
            if d1-d0 >= thresh+2:
                ans += 1
    
    return ans

def solve_2(maze:list[str], thresh:int) -> int:
    R,C = len(maze),len(maze[0])
    path = get_path(maze)
    ans = 0

    coord_to_dist = {}
    for i in range(len(path)):
        coord_to_dist[path[i]] = i
    
    for cheat_sta in path:
        d0 = coord_to_dist[cheat_sta]
        #Cheats of 1s never leave the track
        for cheat_dur in range(2,21):
            cheat_ends = get_mht_dist_away(cheat_sta,R,C,cheat_dur)
            for cheat_end in cheat_ends:
                if cheat_end not in coord_to_dist:
                    continue
                d1 = coord_to_dist[cheat_end]
                #Account for the cheat duration
                if d1-d0 >= thresh+cheat_dur:
                    ans += 1
    
    return ans

with open('Input.txt', 'r') as f:
    txt = f.read()

maze:list[str] = txt.split('\n')
R,C = len(maze),len(maze[0])

print(solve_1(maze,100))
print(solve_2(maze,100))
