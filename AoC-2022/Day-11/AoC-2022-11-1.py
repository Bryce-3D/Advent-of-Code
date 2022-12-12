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
f = [lambda x: (x*7)//3,
     lambda x: (x+4)//3,
     lambda x: (x+2)//3,
     lambda x: (x+7)//3,
     lambda x: (x*17)//3,
     lambda x: (x+8)//3,
     lambda x: (x+6)//3,
     lambda x: (x*x)//3]

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
for Homu in range(20):   #20 cycles
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



'''Recycling bin
def f0(x):
    if x%17 == 0:
        return 5
    else:
        return 3

def f1(x):
    if x%3 == 0:
        return 0
    else:
        return 3

def f2(x):
    if x%5 == 0:
        return 7
    else:
        return 4

def f3(x):
    if x%7 == 0:
        return 5
    else:
        return 2

def f4(x):
    if x%11 == 0:
        return 1
    else:
        return 6

def f5(x):
    if x%19 == 0:
        return 2
    else:
        return 7

def f6(x):
    if x%2 == 0:
        return 0
    else:
        return 1

def f7(x):
    if 

def is_div(d):
    return lambda x: x%d == 0
test = [is_div(i) for i in [17, 3, 5, 7, 11, 19, 2, 13]]

test = [lambda x: x%17 == 0,
        lambda x: x%3 == 0,
        lambda x: x%5 == 0,
        lambda x: x%7 == 0,
        lambda x: x%11 == 0,
        lambda x: x%19 == 0,
        lambda x: x%2 == 0,
        lambda x: x%13 == 0]
'''
