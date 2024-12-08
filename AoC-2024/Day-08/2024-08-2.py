with open('Input.txt', 'r') as f:
    txt = f.read()

def gcd(a,b):
    '''Returns None if a or b is 0'''
    if a == 0 or b == 0:
        return None
    a,b = abs(a),abs(b)
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

M = txt.split('\n')
R,C = len(M),len(M[0])

#poses[c] = list of positions of c
poses = {}
for r in range(R):
    for c in range(C):
        if M[r][c] == '.':
            continue
        char = M[r][c]
        if char not in poses:
            poses[char] = [[r,c]]
        else:
            poses[char].append([r,c])

hit = [[0 for c in range(C)] for r in range(R)]
for char in poses:
    pos = poses[char]
    for i in range(len(pos)):
        for j in range(i):
            #Extract the positions of the same chars
            r_0,c_0 = pos[i]
            r_1,c_1 = pos[j]

            #Corner case of horizontal/vertical lines
            if r_0 == r_1:
                for c in range(C):
                    hit[r_0][c] = 1
                continue
            if c_0 == c_1:
                for r in range(R):
                    hit[r][c_0] = 1
                continue

            #Get the minimal movement along their line
            d_r,d_c = r_1-r_0,c_1-c_0
            d = gcd(d_r,d_c)
            d_r,d_c = d_r//d,d_c//d

            #Go backwards
            r,c = r_0,c_0
            while 0 <= r < R and 0 <= c < C:
                hit[r][c] = 1
                r -= d_r
                c -= d_c

            #Go forwards
            r,c = r_0,c_0
            while 0 <= r < R and 0 <= c < C:
                hit[r][c] = 1
                r += d_r
                c += d_c

ans = sum([sum(i) for i in hit])
print(ans)
