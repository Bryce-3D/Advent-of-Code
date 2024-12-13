with open("Sample.txt", 'r') as f:
    txt = f.read()
tc_txts = txt.split('\n\n')

'''IDEA
Part 1
Note that it is essentially a system of linear equations
Button A = [A_x,A_y]
Button B = [B_x,B_y]
Prize    = [p_x,p_y]

Use button A a times and button B b times means
    p_x = a*A_x + b*B_x
    p_y = a*A_y + b*B_y
'''

def ceil_div(a:int,b:int) -> int:
    return (a-1)//b + 1

def gcd(a:int,b:int) -> int:
    a,b = abs(a),abs(b)
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

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

def has_0_movement_along_one_axis(tc_txt:str) -> bool:
    '''After checking, no test cases have a movement of 0'''
    info = parse_tc(tc_txt)
    return 0 in info

def diophantine(a:int,b:int) -> list[int]:
    '''Return an integer solution [x,y] to ax+by=gcd(a,b)'''
    if a == 0:
        return [0,1]
    if b == 0:
        return [1,0]
    if a%b == 0:
        return [1, 1-a//b]
    if b%a == 0:
        return [1-b//a, 1]
    if a < b:
        return diophantine(b,a)[::-1]
    
    '''
        a = qb + r
        gcd(a,b) = gcd(b,r)
            = xb + yr
            = xb + y(a-qb)
            = ya + (x-yq)b
    '''
    q, r = a//b, a%b
    x,y = diophantine(b,r)
    return [y, x-y*q]

def solve(x_0,x_1,y_0,y_1,c_0,c_1) -> list[int]|None:
    '''
    Solve the system of linear equations
        x_0 x + y_0 y = c_0
        x_1 x + y_1 y = c_1
    
    Returns
    -------
    If the lines are not parallel
        The solution [x,y] if it is an integer solution
        None if it has no integer solution
    If the lines are parallel
        [m_x,k_x,,m_y,k_y] if the general solution is of the form
            (x,y) = (m_x*t+k_x, m_y*t+k_y)'
        for any integer t
        None if it has no integer solution
    The solution [x,y] if a unique integer solution exists
    True if there are infinitely many integer solutions
    False if there are 0 integer solutions
    '''
    D   = x_0*y_1 - x_1*y_0
    D_x = c_0*y_1 - c_1*y_0
    D_y = x_0*c_1 - x_1*c_0

    #If the two lines have different slopes
    if D != 0:
        if D_x%D != 0 or D_y%D != 0:
            return None
        else:
            return [D_x//D,D_y//D]
    
    d = gcd(x_0,y_0)
    #The two lines are parallel and non-overlapping
    if x_0*c_1 != x_1*c_0:
        return None
    #The lines overlap but no integer solution
    if c_0%d != 0:
        return None
    #Find a base solution
    base_sol = diophantine(x_0,y_0)
    base_sol = [i * c_0//d for i in base_sol]
    shift_sol = [y_0//d, -x_0//d]
    return [base_sol[0],shift_sol[0],base_sol[1],shift_sol[1]]

def min_cost(A_x,A_y,B_x,B_y,p_x,p_y) -> int:
    '''
    Returns the min cost to get the prize or 0 if the prize 
    is unreacable.
    '''
    sol = solve(A_x,B_x,A_y,B_y,p_x,p_y)

    print(sol)

    #No solution
    if sol == None:
        return 0
    #One solution
    if len(sol) == 2:
        return 3*sol[0] + sol[1]
    
    return 0
    #Infinite solutions
    '''
        m_a*t + k_a button A presses
        m_b*b + k_b button B presses

        (3m_a+m_b)t + (3k_a+k_b) cost

        Either maximize or minimize t such that both remain positive
    '''
    m_a,k_a,m_b,k_b = sol

    min_t,max_t = None

    #Bound t for button A to have a nonnegative number of presses
    if m_a >= 0:
        return 0



ans = 0
for tc_txt in tc_txts:
    ans += min_cost(*parse_tc(tc_txt))
print(ans)
