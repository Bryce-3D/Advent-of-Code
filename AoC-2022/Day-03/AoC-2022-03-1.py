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

for items in a:
    #Get each bag
    l = len(items)
    k = l//2
    s1 = items[0:k]
    s2 = items[k:l]

    #Find the common item
    for x in s1:
        if x in s2:
            common = x
    
    #Add the value of the common item
    ans += prio[common]

print(ans)
