import re

with open('Input.txt', 'r') as f:
    txt = f.read()
tc_txts = txt.split('\n\n')

def parse_tc_re(tc_txt:str) -> list[int]:
    '''
    Output is
        [A_x, A_y, B_x, B_y, p_x, p_y]
    '''
    return [int(i) for i in re.findall(r'\d+', tc_txt)]

def solve(x_0,x_1,y_0,y_1,c_0,c_1) -> list[int]|None:
    '''
    Solve the system of diophantine equations
        x_0 * x + y_0 * y = c_0
        x_1 * x + y_1 * y = c_1
    
    Assumes that the two lines have different slopes
    Returns [x,y] if an integer solution exists and None otherwise
    '''
    D_x = c_0*y_1 - c_1*y_0
    D_y = x_0*c_1 - x_1*c_0
    D   = x_0*y_1 - x_1*y_0
    if (D_x%D != 0) or (D_y%D != 0):
        return None
    return [D_x//D,D_y//D]

def cost(A_x,A_y,B_x,B_y,p_x,p_y,C) -> int:
    if A_x*B_y == A_y*B_x:
        print('Parallel case found, do by hand')
        print(A_x,A_y,B_x,B_y,p_x,p_y)
        print()
        return 0
    
    moves = solve(A_x,A_y,B_x,B_y,p_x+C,p_y+C)

    if moves == None:
        return 0
    a,b = moves
    return 3*a+b

#Part 1
ans = 0
for tc_txt in tc_txts:
    ans += cost(*parse_tc_re(tc_txt), 0)
print(ans)

#Part 2
C = 10000000000000   #10^13
ans = 0
for tc_txt in tc_txts:
    ans += cost(*parse_tc_re(tc_txt), C)
print(ans)





#Recycling Bin ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def parse_tc(tc_txt:str) -> list[int]:
    '''
    Output is
        [A_x, A_y, B_x, B_y, p_x, p_y]
    '''
    but_A,but_B,prize = tc_txt.split('\n')
    but_A = but_A.split(':')[1]
    but_B = but_B.split(':')[1]
    prize = prize.split(':')[1]
    A_x = int(but_A.split(',')[0][3:])
    A_y = int(but_A.split(',')[1][3:])
    B_x = int(but_B.split(',')[0][3:])
    B_y = int(but_B.split(',')[1][3:])
    p_x = int(prize.split(',')[0][3:])
    p_y = int(prize.split(',')[1][3:])
    return [A_x,A_y,B_x,B_y,p_x,p_y]
