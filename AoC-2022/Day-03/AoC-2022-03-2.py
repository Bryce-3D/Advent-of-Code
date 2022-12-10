#Retrieving the info
f = open('AoC-2022-03-Input.txt', 'r')
a = f.read().split('\n')
f.close()

#prio[x] = priority of item x
prio = {}
for i in range(26):
    smol = chr(ord('a')+i)   #ith small letter
    big = chr(ord('A')+i)    #ith big letter
    prio[smol] = i+1
    prio[big] = i+27

#Remove the empty string at the end
a.pop()

ans = 0

for i in range(len(a)//3):
    #Get the next group of 3 bags
    s0 = a[3*i]
    s1 = a[3*i+1]
    s2 = a[3*i+2]

    #Find the item common to all 3 bags
    for x in s0:
        if x in s1 and x in s2:
            common = x
    
    #Add the priority to the total
    ans += prio[common]

print(ans)
