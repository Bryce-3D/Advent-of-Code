with open('Input.txt', 'r') as f:
    txt = f.read()

l_0,l_1 = [],[]
for line in txt.split('\n'):
    line = [int(i) for i in line.split()]
    l_0.append(line[0])
    l_1.append(line[1])

c_0,c_1 = {},{}
for i in l_0:
    c_0[i] = c_0.get(i,0)+1
for i in l_1:
    c_1[i] = c_1.get(i,0)+1

ans = 0
for k in c_0:
    ans += k * c_0[k] * c_1.get(k,0)

print(ans)
