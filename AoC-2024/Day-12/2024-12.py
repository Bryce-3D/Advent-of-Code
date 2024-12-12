with open('Input.txt', 'r') as f:
    txt = f.read()

def flood_fill_1(M:list[str],seen:list[list[bool]], r0:int, c0:int) -> int:
    '''IDEA
    Flood fill each region
    Area = Number of cells
    For perimeter:
        For each square in the region
        Adjacent to k others in the region -> +(4-k) to the perimeter
        Sum this over all the squares in the region
    '''
    #N,S,W,E directions
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]

    if seen[r0][c0]:
        return 0
    R,C = len(M),len(M[0])
    char = M[r0][c0]

    perimeter,area = 0,0

    seen[r0][c0] = True
    BFS = [[r0,c0]]
    ind = 0
    while ind < len(BFS):
        r,c = BFS[ind]
        ind += 1

        #Update perimeter and area
        area += 1
        for dir in dirs:
            r_,c_ = r+dir[0],c+dir[1]
            if not (0 <= r_ < R and 0 <= c_ < C):
                perimeter += 1
            elif M[r_][c_] != char:
                perimeter += 1
        
        #BFS towards neighbors
        for dir in dirs:
            r_,c_ = r+dir[0],c+dir[1]
            if not (0 <= r_ < R and 0 <= c_ < C):
                continue
            if M[r_][c_] != char:
                continue
            if seen[r_][c_]:
                continue
            seen[r_][c_] = True
            BFS.append([r_,c_])

    return perimeter*area

def area(region:list[list[bool]]) -> int:
    R,C = len(region),len(region[0])
    ans = 0
    for r in range(R):
        for c in range(C):
            if region[r][c]:
                ans += 1
    return ans

def num_sides(region:list[list[bool]]) -> int:
    R,C = len(region),len(region[0])
    ans = 0

    #Trace along horizontal grid lines
    for r in range(R-1):
        on = False
        for c in range(C):
            #Both in or out of the region -> no border
            if region[r][c] == region[r+1][c]:
                on = False
            #Start of a new side
            elif not on:
                ans += 1
                on = True
            #New side from flipping
            elif region[r][c] != region[r][c-1]:
                ans += 1

    #Trace along vertical grid lines
    for c in range(C-1):
        on = False
        for r in range(R):
            #Both in or out of the region -> no border
            if region[r][c] == region[r][c+1]:
                on = False
            #Start of a new side
            elif not on:
                ans += 1
                on = True
            #New side from flipping
            elif region[r][c] != region[r-1][c]:
                ans += 1

    #N border
    on = False
    for c in range(C):
        #Not in the region -> no border
        if not region[0][c]:
            on = False
        #Start of a new side
        elif not on:
            ans += 1
            on = True
    #S border
    on = False
    for c in range(C):
        #Not in the region -> no border
        if not region[R-1][c]:
            on = False
        #Start of a new side
        elif not on:
            ans += 1
            on = True
    #W border
    on = False
    for r in range(R):
        #Not in the region -> no border
        if not region[r][0]:
            on = False
        #Start of a new side
        elif not on:
            ans += 1
            on = True
    #E border
    on = False
    for r in range(R):
        #Not in the region -> no border
        if not region[r][C-1]:
            on = False
        #Start of a new side
        elif not on:
            ans += 1
            on = True
    
    return ans

def brute_force_flood_fill_2(M:list[str],seen:list[list[bool]], r0:int, c0:int) -> int:
    #N,S,W,E directions
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]

    if seen[r0][c0]:
        return 0
    R,C = len(M),len(M[0])
    char = M[r0][c0]

    seen[r0][c0] = True
    BFS = [[r0,c0]]
    ind = 0
    region = [[False for c in range(C)] for r in range(R)]

    while ind < len(BFS):
        r,c = BFS[ind]
        ind += 1
        region[r][c] = True
        
        #BFS towards neighbors
        for dir in dirs:
            r_,c_ = r+dir[0],c+dir[1]
            if not (0 <= r_ < R and 0 <= c_ < C):
                continue
            if M[r_][c_] != char:
                continue
            if seen[r_][c_]:
                continue
            seen[r_][c_] = True
            BFS.append([r_,c_])

    return num_sides(region)*area(region)

def count_corners(M:list[str], r:int, c:int) -> int:
    '''
    Count the number of corners at (r0,c0) from the 
    region containing (r0,c0)

    Corner Types (NW perspective)
    Type 1    Type 2
      X       X|O
     +-       -+
    X|O       O O

    *O = in, X = out, + = corner
    '''
    char = M[r][c]
    ans = 0
    #NW corner
    if r == 0 and c == 0:
        ans += 1
    elif r == 0:
        if M[r][c-1] != char:
            ans += 1
    elif c == 0:
        if M[r-1][c] != char:
            ans += 1
    else:
        type_1 = M[r-1][c] != char and M[r][c-1] != char
        type_2 = M[r-1][c] == char and M[r][c-1] == char and M[r-1][c-1] != char
        if type_1 or type_2:
            ans += 1
    #NE corner
    if r == 0 and c == C-1:
        ans += 1
    elif r == 0:
        if M[r][c+1] != char:
            ans += 1
    elif c == C-1:
        if M[r-1][c] != char:
            ans += 1
    else:
        type_1 = M[r-1][c] != char and M[r][c+1] != char
        type_2 = M[r-1][c] == char and M[r][c+1] == char and M[r-1][c+1] != char
        if type_1 or type_2:
            ans += 1
    #SW corner
    if r == R-1 and c == 0:
        ans += 1
    elif r == R-1:
        if M[r][c-1] != char:
            ans += 1
    elif c == 0:
        if M[r+1][c] != char:
            ans += 1
    else:
        type_1 = M[r+1][c] != char and M[r][c-1] != char
        type_2 = M[r+1][c] == char and M[r][c-1] == char and M[r+1][c-1] != char
        if type_1 or type_2:
            ans += 1
    #SE corner
    if r == R-1 and c == C-1:
        ans += 1
    elif r == R-1:
        if M[r][c+1] != char:
            ans += 1
    elif c == C-1:
        if M[r+1][c] != char:
            ans += 1
    else:
        type_1 = M[r+1][c] != char and M[r][c+1] != char
        type_2 = M[r+1][c] == char and M[r][c+1] == char and M[r+1][c+1] != char
        if type_1 or type_2:
            ans += 1
    
    return ans

def better_flood_fill_2(M:list[str], seen:list[list[bool]], 
        r0:int, c0:int) -> int:
    '''IDEA
    Note that the number of sides = the number of corners
    And there are only two kinds of corners (O = in region)

        X|O   O|X
        -+    -+
        O O   X X
    '''
    #N,S,W,E directions
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]

    if seen[r0][c0]:
        return 0
    R,C = len(M),len(M[0])
    char = M[r0][c0]

    sides,area = 0,0

    seen[r0][c0] = True
    BFS = [[r0,c0]]
    ind = 0
    region = [[False for c in range(C)] for r in range(R)]

    while ind < len(BFS):
        r,c = BFS[ind]
        ind += 1
        region[r][c] = True

        #Update sides and area
        sides += count_corners(M,r,c)
        area += 1
        
        #BFS towards neighbors
        for dir in dirs:
            r_,c_ = r+dir[0],c+dir[1]
            if not (0 <= r_ < R and 0 <= c_ < C):
                continue
            if M[r_][c_] != char:
                continue
            if seen[r_][c_]:
                continue
            seen[r_][c_] = True
            BFS.append([r_,c_])

    return sides*area



M = txt.split('\n')
R,C = len(M),len(M[0])

#Part 1
seen = [
    [False for c in range(C)]
    for r in range(R)
]
ans = 0
for r in range(R):
    for c in range(C):
        ans += flood_fill_1(M,seen,r,c)
print(ans)

#Part 2 (Brute Force)
seen = [
    [False for c in range(C)]
    for r in range(R)
]
ans = 0
for r in range(R):
    for c in range(C):
        ans += brute_force_flood_fill_2(M,seen,r,c)
print(ans)

#Part 2 (Clever)
seen = [
    [False for c in range(C)]
    for r in range(R)
]
ans = 0
for r in range(R):
    for c in range(C):
        ans += better_flood_fill_2(M,seen,r,c)
print(ans)
