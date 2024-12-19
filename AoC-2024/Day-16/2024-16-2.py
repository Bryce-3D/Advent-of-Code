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

def mark_backtrack(
        is_in_shortest_path:dict[tuple[int,int],list[list[bool]]],
        parents:dict[
            tuple[int,int],
            list[list[
                list[
                    tuple[
                        tuple[int,int],
                        tuple[int,int],
                    ]
                ]
            ]]
        ],
        drt:tuple[int,int], r:int, c:int) -> None:
    #Already marked -> No need to redo the whole thing
    if is_in_shortest_path[drt][r][c]:
        return
    #Not yet marked -> Mark
    is_in_shortest_path[drt][r][c] = True
    #And backtrack along everything before it
    for par in parents[drt][r][c]:
        prev_coord,prev_drt = par
        mark_backtrack(
            is_in_shortest_path,
            parents,
            prev_drt,
            prev_coord[0],
            prev_coord[1],
        )

ALL_DRTS = [
    (-1, 0),
    ( 1, 0),
    ( 0,-1),
    ( 0, 1),
]





with open('Input.txt', 'r') as f:
    txt = f.read()
maze = txt.split('\n')
R,C = len(maze),len(maze[0])

#dists[drt] = matrix of distances for a given direction
dists:dict[
    tuple[int,int],
    list[list[
        int|None
    ]]
] = {
    drt : [[None for c in range(C)] for r in range(R)]
    for drt in ALL_DRTS
}
#parents[drt][r][c] = list of parents of the corresponding states, 
#i.e. the set of states that can lead to this with the 
#least possible distance. States are (coord,drt)
parents:dict[
    tuple[int,int],               #Direction to
    list[list[                    #Matrix of
        list[                     #List of
            tuple[                #Tuple of
                tuple[int,int],   #Coordinate and
                tuple[int,int],   #Direction
            ]
        ]
    ]]
] = {
    drt : [[[] for c in range(C)] for r in range(R)]
    for drt in ALL_DRTS
}
#Contains elements of the form 
#    (dist, (coord,drt,par_coord,par_drt))
frontier = PQ()
frontier.put((
    0,                    #Distance
    (
        find_sta(maze),   #Coordinate
        (0,1),            #Direction
        None,             #Parent Coordinate
        None,             #Parent Direction
    )
))





#Run Dijkstra's while keeping track of all parents
while frontier.qsize() > 0:
    dist,state = frontier.get()
    coord,drt,par_coord,par_drt = state
    r,c = coord

    #Already explored with a better distance
    if dists[drt][r][c] != None and dists[drt][r][c] < dist:
        continue
    #Already explored with the same distance or not yet explored
    # -> Record as a parent
    if par_coord != None and par_drt != None:
        parents[drt][r][c].append(
            (par_coord,par_drt)
        )
    #Already explored with the same distance
    if dists[drt][r][c] != None and dists[drt][r][c] == dist:
        continue
    #Else not yet explored -> Update the distance
    dists[drt][r][c] = dist

    #Check all the neighbors
    #Move forwards
    r1,c1 = r+drt[0],c+drt[1]
    if 0 <= r1 < R and 0 <= c1 < C:
        if maze[r1][c1] != '#':
            new_coord = (r1,c1)
            frontier.put((
                dist+1,
                (
                    new_coord,   #Coord of new state to explore
                    drt,         #Drt of new state to explore
                    coord,       #Coord of parent aka current coord
                    drt,         #Drt of parent aka current drt
                )
            ))
    #Turn left
    frontier.put((
        dist+1000,
        (
            coord,
            turn_right(drt),
            coord,
            drt,
        )
    ))
    #Turn right
    frontier.put((
        dist+1000,
        (
            coord,
            turn_right(drt),
            coord,
            drt,
        )
    ))





#Now check which states are on a shortest path by backtracking
end_r,end_c = find_end(maze)
min_dist = min([
    dists[drt][end_r][end_c]
    for drt in ALL_DRTS
])

is_in_shortest_path:dict[tuple[int,int],list[list[bool]]] = {
    drt : [[False for c in range(C)] for r in range(R)]
    for drt in ALL_DRTS
}

for end_drt in ALL_DRTS:
    #Not an optimal ending direction -> skip backtracking
    if dists[end_drt][end_r][end_c] != min_dist:
        continue
    #Is an optimal ending direction -> run backtracking
    mark_backtrack(
        is_in_shortest_path,
        parents,
        end_drt,
        end_r,
        end_c
    )

is_in_shortest_path_cells:list[list[int]] = [
    [0 for c in range(C)]
    for r in range(R)
]
for drt in ALL_DRTS:
    for r in range(R):
        for c in range(C):
            if is_in_shortest_path[drt][r][c]:
                is_in_shortest_path_cells[r][c] = 1

ans = sum([
    sum(row) for row in is_in_shortest_path_cells
])
print(ans)
