with open('Input.txt', 'r') as f:
    txt = f.read()
tc_txts = txt.split('\n\n')

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

def solve_1(A_x,A_y,B_x,B_y,p_x,p_y):
    for a in range(101):
        for b in range(101):
            if A_x*a + B_x*b != p_x:
                continue
            if A_y*a + B_y*b != p_y:
                continue
            return 3*a+b
    return 0

ans = 0
for tc_txt in tc_txts:
    ans += solve_1(*parse_tc(tc_txt))
print(ans)
