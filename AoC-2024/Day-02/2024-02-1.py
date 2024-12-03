with open('Input.txt', 'r') as f:
    txt = f.read()
txt_lines = txt.split('\n')

ans = 0
for line in txt_lines:
    line = [int(i) for i in line.split()]

    #Line has only 1 report
    if len(line) == 1:
        ans += 1
    
    diffs = [line[i+1]-line[i] for i in range(len(line)-1)]
    m,M = min(diffs),max(diffs)
    if 1 <= m and M <= 3:
        ans += 1
    if -3 <= m and M <= -1:
        ans += 1

print(ans)
