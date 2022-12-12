'''Manually encode the info'''
#items[i] = list of items currently held by monke i
items = [[54, 89, 94],                       #0
         [66, 71],                           #1
         [76, 55, 80, 55, 55, 96, 78],       #2
         [93, 69, 76, 66, 89, 54, 59, 94],   #3
         [80, 54, 58, 75, 99],               #4
         [69, 70, 85, 83],                   #5
         [89],                               #6
         [62, 80, 58, 57, 93, 56]]           #7

#f[i] = function to update the worry lvl after the 
#ith monke inspects an item
#Note that we only need to track the numbers modulo 
#the lcm of all the divisibility tests
lcm = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
f = [lambda x: (x*7)%lcm,
     lambda x: (x+4)%lcm,
     lambda x: (x+2)%lcm,
     lambda x: (x+7)%lcm,
     lambda x: (x*17)%lcm,
     lambda x: (x+8)%lcm,
     lambda x: (x+6)%lcm,
     lambda x: (x*x)%lcm]

#Returns a function f such that 
#   f(x) = yes   if r|x
#   f(x) = no    otherwise
def monkey_f(r,yes,no):
    def created_f(x):
        if x%r == 0:
            return yes
        else:
            return no
    
    return created_f
#next[i] = The function monkey i uses to determine 
#where to throw an item with a given worry level
next = [monkey_f(17,5,3),   #0
        monkey_f(3,0,3),    #1
        monkey_f(5,7,4),    #2
        monkey_f(7,5,2),    #3
        monkey_f(11,1,6),   #4
        monkey_f(19,2,7),   #5
        monkey_f(2,0,1),    #6
        monkey_f(13,6,4)]   #7

#insp[i] = number of items inspected by the ith monke so far
insp = [0 for i in range(8)]



'''Actually doing the item'''
#Performing the process
#Also note that the order in which items are thrown by a 
#specific monke during its turn doesn't matter.
for Homu in range(10000):   #10000 cycles
    for i in range(8):   #For each monke
        #Inspect and throw every item held by the ith monke
        while len(items[i]) != 0:
            item = items[i].pop()     #Get the next item's worry lvl
            item = f[i](item)         #Update the item's worry lvl
            i_0 = next[i](item)       #Find who to toss it to
            items[i_0].append(item)   #Throw it
            insp[i] += 1              #Increment number of inspected items

#Find the ans
insp.sort()
print(insp[-1] * insp[-2])
