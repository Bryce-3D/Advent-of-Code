with open('Sample.txt', 'r') as f:
    txt = f.read()

rules_txt,order_txt = txt.split('\n\n')

rules = [
    [int(i) for i in line.split('|')]
    for line in rules_txt.split('\n')
]
orders = [
    [int(i) for i in line.split(',')]
    for line in order_txt.split('\n')
]

ans = 0
for order in orders:
    works = True
    for i in range(len(order)-1):
        l,r = order[i],order[i+1]
        if [r,l] in rules:
            works = False
            break
    if works:
        l = len(order)
        ans += order[l//2]

print(ans)
