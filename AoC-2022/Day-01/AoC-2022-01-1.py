#Retrieving the info
f = open('AoC-2022-01-Input.txt', 'r')
l = f.read().split('\n')
f.close()

curr = 0
M = 0
for val in l:
    if val == '':   #If divider
        M = max(curr, M)
        curr = 0
    else:           #If next value
        curr += int(val)

print(M)
