#For sorting by comparator rather than key
from functools import cmp_to_key

#Retrieving the info
f = open('AoC-2022-13-Input.txt', 'r')
inp = f.read().split('\n')
f.close()

#Parsing the info
l = len(inp)//3   #Kept the extra newline at the end
a = []           #Processed list of packets
#Append each of the l pairs
for i in range(l):
    a.append(eval(inp[3*i]))
    a.append(eval(inp[3*i+1]))
#Add the dividers
div4 = [[2]]
div3 = [[6]]
a.append(div4)
a.append(div3)



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



#Sort and get the ans
a = sorted(a, key=cmp_to_key(comp))
i0 = a.index(div4) + 1
i1 = a.index(div3) + 1
ans = i0 * i1
print(ans)
