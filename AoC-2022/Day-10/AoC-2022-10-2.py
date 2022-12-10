#Retrieving the info
f = open('AoC-2022-10-Input.txt', 'r')
a = f.read().split('\n')
f.close()

X = 1
cyc = 0   #0-index cycle count instead
CRT = [[' ' for c in range(40)] for r in range(6)]

for op in a:
    op = op.split()

    #Process current cycle
    r = cyc//40
    c = cyc%40

    if abs(c-X) <= 1:
        CRT[r][c] = '#'
    else:
        CRT[r][c] = '.'
    
    cyc += 1

    #Do more if it's addx
    if op[0] == 'addx':
        r = cyc//40
        c = cyc%40

        if abs(c-X) <= 1:
            CRT[r][c] = '#'
        else:
            CRT[r][c] = '.'
        
        cyc += 1

        V = int(op[1])
        X += V

CRT = [''.join(row) for row in CRT]
for row in CRT:
    print(row)
