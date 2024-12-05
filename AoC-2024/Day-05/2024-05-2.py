with open('Sample.txt', 'r') as f:
    txt = f.read()

#Seems to be a total ordering
#1176 -> 49 pages to print

'''IDEA
0th iff left on 49 pairs
1st iff left on 48 pairs
...

0th iff right on 0 pairs
1st iff right on 1 pair
...
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

exit(0)

left_count = {}
right_count = {}
for rule in rules:
    l,r = rule
    left_count[l] = left_count.get(l,0)+1
    right_count[r] = right_count.get(r,0)+1

# print(left_count)
# print(right_count)
# print(len(left_count))
# print(rules[:10])

print(left_count)
print(right_count)

for i in left_count:
    print(i, left_count[i])

n = len(left_count)+1
order = [-1 for i in range(n)]
for k in left_count:
    order[n-1-left_count[k]] = k
for k in right_count:
    order[right_count[k]] = k

print(order)
