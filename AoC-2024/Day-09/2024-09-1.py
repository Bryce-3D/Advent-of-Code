with open('Input.txt', 'r') as f:
    txt = f.read()

#95288 positions in memory, brute forcable
n = 0
for c in txt:
    n += int(c)
# print(n)

a = [None for i in range(n)]
id = 0
ind = 0
for Homu in range(len(txt)):
    k = int(txt[Homu])
    #Empty space
    if Homu%2 == 1:
        ind += k
        continue
    #Write the file id
    for i in range(k):
        a[ind] = id
        ind += 1
    #Increment to next file id
    id += 1

L,R = 0,n-1
while L < R:
    #Filled, so no movement needed
    if a[L] != None:
        L += 1
        continue
    
    #Trace from the right to find the next thing to move
    while L < R and a[R] == None:
        R -= 1
    #If nothing left to move, then done
    if L == R:
        continue
    #If something to move, then move it and continue
    a[L],a[R] = a[R],a[L]

ans = 0
for i in range(n):
    k = a[i]
    if k == None:
        break
    ans += i*k
print(ans)
