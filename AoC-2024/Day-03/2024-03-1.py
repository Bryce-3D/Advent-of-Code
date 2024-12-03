import re

with open('Input.txt', 'r') as f:
    txt = f.read()

#print(len(txt))   #18477

mul_regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')

ans = 0
for thing in mul_regex.finditer(txt):
    s = thing.group(0)
    a,b = [int(i) for i in s[4:-1].split(',')]
    ans += a*b

print(ans)
