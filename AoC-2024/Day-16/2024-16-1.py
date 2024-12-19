'''IDEA
Run Dijkstra's on the set of (position,direction) pairs
'''

from queue import PriorityQueue as PQ

def find_sta(maze:list[str]) -> tuple[int,int]:
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                return r,c
    raise Exception('What')

def find_end(maze:list[str]) -> tuple[int,int]:
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'E':
                return r,c
            
def turn_left(drt:tuple[int,int]) -> tuple[int,int]:
    if drt == (-1,0):
        return (0,-1)
    if drt == (0,-1):
        return (1,0)
    if drt == (1,0):
        return (0,1)
    if drt == (0,1):
        return (-1,0)
    raise Exception(f'Invalid drt: {drt}')

def turn_right(drt:tuple[int,int]) -> tuple[int,int]:
    if drt == (-1,0):
        return (0,1)
    if drt == (0,1):
        return (1,0)
    if drt == (1,0):
        return (0,-1)
    if drt == (0,-1):
        return (-1,0)
    raise Exception(f'Invalid drt: {drt}')

with open('Input.txt', 'r') as f:
    txt = f.read()

maze = txt.split('\n')
R,C = len(maze),len(maze[0])

all_drts = [
    (-1, 0),
    ( 1, 0),
    ( 0,-1),
    ( 0, 1),
]

#dists[drt] = matrix of distances
dists = {
    drt : [[None for c in range(C)] for r in range(R)]
    for drt in all_drts
}

#Contains elements of the form (dist, (coordinate,dir))
#coordinate = (r,c), drt = (-1,0), etc
frontier = PQ()
frontier.put((0,(find_sta(maze), (0,1))))

while frontier.qsize() > 0:
    dist,state = frontier.get()
    coord, drt = state
    r,c = coord

    #Already explored
    if dists[drt][r][c] != None:
        continue

    #Update the distance 
    dists[drt][r][c] = dist

    #Move forward
    r1,c1 = r+drt[0],c+drt[1]
    if 0 <= r1 < R and 0 <= c1 < C:
        if maze[r1][c1] != '#':
            new_coord = (r1,c1)
            frontier.put((
                dist+1,
                (new_coord,drt)
            ))
    
    #Turn left
    frontier.put((
        dist+1000,
        (coord,turn_left(drt))
    ))
    #Turn right
    frontier.put((
        dist+1000,
        (coord,turn_right(drt))
    ))

end_r,end_c = find_end(maze)
ans = min([
    dists[drt][end_r][end_c] 
    for drt in all_drts
])
print(ans)
