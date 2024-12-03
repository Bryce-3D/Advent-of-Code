import re

with open('Input.txt', 'r') as f:
    txt = f.read()

mul_regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
def mul(s:str) -> int:
    m = mul_regex.match(s)
    if m == None:
        return 0
    m = m.group(0)
    a,b = m[4:-1].split(',')
    return int(a)*int(b)

ans = 0
on = True
for i in range(len(txt)):
    if txt[i:i+4] == 'do()':
        on = True
        continue
    if txt[i:i+7] == 'don\'t()':
        on = False
        continue
    if not on:
        continue
    s = txt[i:i+12]
    ans += mul(s)

print(ans)
