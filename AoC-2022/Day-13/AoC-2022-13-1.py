#Retrieving the info
f = open('AoC-2022-13-Input.txt', 'r')
a = f.read().split('\n')
f.close()



#For convenience
inst = isinstance
'''
Takes in two packets a,b and compares them recursively
Returns
    -1   if a < b
     0   if a = b
     1   if a > b
'''
def comp(a,b):
    #If both are integers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if inst(a, int) and inst(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    
    #If only a is an integer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif inst(a, int) and inst(b, list):
        return comp([a],b)   #Package a in a list and compare
    
    #If only b is an integer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif inst(a, list) and inst(b, int):
        return comp(a,[b])   #Package b in a list and compare
    
    #If neither of a,b are integers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    m = min(len(a), len(b))   #Compare until one runs out
    for i in range(m):
        k = comp(a[i], b[i])   #Compare the ith element
        if k != 0:             #If they are not the same
            return k           #Return the result
    #One has run out, so compare lengths
    return comp(len(a), len(b))



# *Kept the extra newline at the end
l = len(a)//3
ans = 0

#Check for each of the l pairs
for i in range(l):
    a0 = eval(a[3*i])
    a1 = eval(a[3*i+1])
    if comp(a0,a1) <= 0:   #if L<=R
        ans += i+1

print(ans)
