#Retrieving the info
f = open('AoC-2022-10-Input.txt', 'r')
a = f.read().split('\n')
f.close()

X = 1
cyc = 1   #Current cycle number
ans = 0

for op in a:
    op = op.split()

    if op[0] == 'noop':
        cyc += 1
        if cyc%40 == 20:
            ans += cyc * X
    
    else:
        V = int(op[1])

        cyc += 1
        if cyc%40 == 20:
            ans += cyc * X
        
        cyc += 1
        X += V
        if cyc%40 == 20:
            ans += cyc * X

print(ans)
