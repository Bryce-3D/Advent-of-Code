with open('Input.txt', 'r') as f:
    txt = f.read()

'''IDEA
(Guaranteed) in the middle iff it is forced to have 
n//2 items on each side by the rules
'''

rules_txt,order_txt = txt.split('\n\n')

rules = [
    [int(i) for i in line.split('|')]
    for line in rules_txt.split('\n')
]
orders = [
    [int(i) for i in line.split(',')]
    for line in order_txt.split('\n')
]

def solve(line) -> int:
    n = len(line)
    in_order = True
    for i in range(n-1):
        if [line[i+1],line[i]] in rules:
            in_order = False
            break
    if in_order:
        return 0
    right_count = {i:0 for i in line}
    for rule in rules:
        l,r = rule[0],rule[1]
        if l in line and r in line:
            right_count[l] += 1
    for k in right_count:
        if right_count[k] == n//2:
            return k
    raise Exception('Answer is not unique')
    
ans = 0
for order in orders:
    ans += solve(order)
print(ans)
