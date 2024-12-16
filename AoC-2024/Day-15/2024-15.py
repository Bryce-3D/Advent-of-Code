with open('Input.txt', 'r') as f:
    txt = f.read()

def parse_txt(txt:str) -> tuple[list[list[str]], str]:
    '''Return [grid, moves]'''
    grid,moves = txt.split('\n\n')
    grid = [[c for c in row] for row in grid.split('\n')]
    moves = ''.join(moves.split('\n'))
    return grid,moves

def drt_str_to_tuple(drt:str) -> tuple[int,int]:
    convert = {
        '^':(-1, 0),
        'v':( 1, 0),
        '<':( 0,-1),
        '>':( 0, 1),
    }
    return convert[drt]

def find_robot(grid:list[list[str]]) -> tuple[int,int]:
    R,C = len(grid),len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@':
                return (r,c)
    raise Exception('No robot in the grid')

def move(grid:list[list[str]], robot_pos:tuple[int,int], 
         drt:tuple[int,int]) -> tuple[int,int]:
    '''
    Update the grid given the robot's position and direction
    Return the robot's new position
    '''
    r_r,r_c = robot_pos
    d_r,d_c = drt
    #Trace through the boxes along the direction
    r,c = r_r+d_r,r_c+d_c
    while grid[r][c] == 'O':   #Will not fall out due to the # border
        r,c = r+d_r,c+d_c
    #If blocked, then do nothing
    if grid[r][c] == '#':
        return r_r,r_c
    #If not blocked, then move and push the boxes
    grid[r][c] = 'O'
    grid[r_r+d_r][r_c+d_c] = '@'
    grid[r_r][r_c] = '.'
    #Return the new robot location
    return r_r+d_r,r_c+d_c

def score(grid:list[list[str]]) -> int:
    R,C = len(grid),len(grid[0])
    ans = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                ans += 100*r+c
    return ans

def part_1(txt:str) -> int:
    grid,moves = parse_txt(txt)
    drts = [drt_str_to_tuple(c) for c in moves]
    robot_pos = find_robot(grid)
    for drt in drts:
        robot_pos = move(grid,robot_pos,drt)
    return score(grid)

print(part_1(txt))
