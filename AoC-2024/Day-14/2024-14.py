import time
import re

with open('Sample.txt', 'r') as f:
    txt = f.read()

def parse_row(row:str) -> list[list[int]]:
    '''Return [pos, vel]'''
    nums = [int(i) for i in re.findall(r'-?\d+', row)]
    return [[nums[0],nums[1]], [nums[2],nums[3]]]

def part_1(txt:str, X:int, Y:int, t:int) -> int:
    X_mid,Y_mid = X//2,Y//2
    Q_count = [[0,0],[0,0]]
    for row in txt.split('\n'):
        pos,vel = parse_row(row)
        end_x = (pos[0] + t*vel[0]) % X
        end_y = (pos[1] + t*vel[1]) % Y
        #Right in the middle
        if end_x == X_mid:
            continue
        if end_y == Y_mid:
            continue
        #Find the quadrant it lies in
        x_side = 0 if end_x < X_mid else 1
        y_side = 0 if end_y < Y_mid else 1
        Q_count[x_side][y_side] += 1
    ans = Q_count[0][0] * Q_count[0][1] * Q_count[1][0] * Q_count[1][1]
    return ans

def get_robots(txt:str) -> list[list[list[int]]]:
    '''
    Get a list where elements are of the form
        [pos,vel]
    '''
    ans = []
    for row in txt.split('\n'):
        ans.append(parse_row(row))
    return ans

def update_robots(robots:list[list[list[int]]], X:int, Y:int) -> None:
    '''Update the state by 1s on an X by Y board'''
    for robot in robots:
        pos,vel = robot
        pos[0] = (pos[0]+vel[0]) % X
        pos[1] = (pos[1]+vel[1]) % Y

def print_robots(robots:list[list[list[int]]], X:int, Y:int) -> None:
    grid = [[' ' for x in range(X)] for y in range(Y)]
    for robot in robots:
        pos_x,pos_y = robot[0]
        grid[pos_y][pos_x] = '█' #'■'
    rows = [''.join(row) for row in grid]
    ans = '\n'.join(rows)
    print(ans)

def part_2(txt:str, X:int, Y:int, t_min:int, t_max:int, pause:float) -> None:
    robots = get_robots(txt)
    for Homu in range(t_min):
        update_robots(robots, X, Y)

    for t in range(t_min,t_max):
        print(f'{t} seconds have passed')
        print_robots(robots, X, Y)
        print()
        update_robots(robots, X, Y)
        time.sleep(pause)



print(part_1(txt,101,103,100))
part_2(txt,101,103,0,10,1)   #?
