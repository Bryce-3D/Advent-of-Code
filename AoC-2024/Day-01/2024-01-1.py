with open('Input.txt', 'r') as f:
    txt = f.read()

l_0,l_1 = [],[]
for line in txt.split('\n'):
    line = [int(i) for i in line.split()]
    l_0.append(line[0])
    l_1.append(line[1])

l_0.sort()
l_1.sort()

ans = 0
for i in range(len(l_0)):
    ans += abs(l_1[i]-l_0[i])

print(ans)
