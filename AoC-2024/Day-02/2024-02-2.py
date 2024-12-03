with open('Input.txt', 'r') as f:
    txt = f.read()
txt_lines = txt.split('\n')

'''IDEA
Each line is quite short
Can just brute force
'''

def works_1(l:list[int]) -> bool:
    diffs = [l[i+1]-l[i] for i in range(len(l)-1)]
    m,M = min(diffs),max(diffs)
    if 1 <= m and M <= 3:
        return True
    if -3 <= m and M <= -1:
        return True
    return False

def works_2(l:list[int]) -> bool:
    if works_1(l):
        return True
    for i in range(len(l)):
        l_ = l.copy()
        l_.pop(i)
        if works_1(l_):
            return True
    return False


ans = 0
for line in txt_lines:
    line = [int(i) for i in line.split()]
    if works_2(line):
        ans += 1

print(ans)
