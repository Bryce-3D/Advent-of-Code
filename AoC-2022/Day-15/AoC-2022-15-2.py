#Out of curiosity for runtime checking
#Expected: 30s to 60s
#Actual: 104.07400012016296s
import time
time_0 = time.time()

#Retrieving the info
f = open('AoC-2022-15-Input.txt', 'r')
inp = f.read().split('\n')
f.close()

#Note to self: some beacons lie on y = 2x10^6

#Parsing the input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Each element of pairs is of the form 
#    [sensor, closest beacon]
#where sensor and closest beacon are coordinates
pairs = []
for line in inp:
    line = line.split()   #Break along whitespaces

    #Get x-coord of sensor
    s_x = line[2]    #2nd block
    s_x = s_x[2:]    #Remove 'x=' from the front
    s_x = s_x[:-1]   #Remove ',' from the back
    s_x = int(s_x)
    
    #Get y-coord of sensor
    s_y = line[3]    #3rd block
    s_y = s_y[2:]    #Remove 'y=' from the front
    s_y = s_y[:-1]   #Remove ':' from the back
    s_y = int(s_y)

    #Get x-coord of closest Beacon
    b_x = line[8]    #8th block
    b_x = b_x[2:]    #Remove 'x=' from the front
    b_x = b_x[:-1]   #Remove ',' from the back
    b_x = int(b_x)

    #Get y-coord of closest Beacon
    b_y = line[9]   #9th block
    b_y = b_y[2:]   #Remove 'y=' from the front
    b_y = int(b_y)

    pair = [[s_x,s_y], [b_x,b_y]]
    pairs.append(pair)



#Actually solving the problem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
Essentially do optimized Day 15-1 until we find a row 
that is not fully swept.

Optimized version: Store intervals rather than indiv values

This will be sufficiently fast even with a naive method of 
maintaining the set of intervals since there are only 
29 beacons, aka O(n^2) is approx 900 ops only.
Done over 4x10^6 rows, this will take approx 36 x 10^8 ops.
This should be able to finish in under a minute.

Updating the intervals could probably be optimized to 
O(nlogn) using binary search but like log_2(30)=5 is not 
exactly a big improvement, and binary search's constant 
factor might be a bit bigger too.
Also the number of intervals within blocc should be small 
for most rows, since it should simply to a single interval 
for the whole thing in most rows.

Wait new idea
Updating the storage of the intervals at each stage is very 
painful. What if I toss in all the intervals, *then* update it.
O(30) to toss in every non-empty interval
O(30log30) to sort by the left ends of each interval
O(30) to check if they all connect together
Check that the current max right end is >= the next left end at 
each step, and check that it reaches both ends at 0 and 4000000.
'''
n = 4000000
for y in range(0,n+1):
    #Array of intervals blocked by each pair for row y
    blocc = []
    #For each sensor-beacon pair
    for pair in pairs:
        #Get the interval along row y blocked by the pair
        sen = pair[0]
        bea = pair[1]
        dist = abs(sen[0]-bea[0]) + abs(sen[1]-bea[1])
        dist_y = abs(sen[1]-y)
        dist_x = dist - dist_y
        #Only include non-empty intervals
        if dist_x >= 0:
            #Trim off anything outside of [0:n+1] too
            min_x = max(sen[0] - dist_x, 0)
            max_x = min(sen[0] + dist_x, n)
            intv = [min_x, max_x+1]   #[x,y] means [x:y]
            blocc.append(intv)
    
    #Sort according to the left ends of each interval
    blocc.sort(key = lambda x: x[0])
    swept = True
    #Left and right ends of the union of a prefix of blocc
    L = blocc[0][0]
    R = blocc[0][1]
    #Union next interval (break if there's any gap)
    for i in range(1, len(blocc)):
        if R < blocc[i][0]:   #If it doesn't connect
            swept = False
            break
        else:   #If it does connect
            R = max(blocc[i][1], R)   #Extend if applicable
    #Check if the sweep reaches the ends
    if L != 0 or R != n+1:
        swept = False
    
    #If the row is not swept, correct row found
    #Intervals and y are still stored in blocc and y, so we 
    #can process them outside
    if not swept:
        break

#Linearly sweep until an unblocked x is found
x = 0
for intv in blocc:
    if intv[0] <= x:   #If x is hit
        x = max(x, intv[1])   #Inc x to next smallest unblocked
    else:   #If x is not hit
        break
#Corner case where the unblocked x is x=n is handed by just 
#iterating till the end and ending with x=n

ans = x*n + y
print(ans)



time_1 = time.time()
duration = time_1 - time_0
print(f'Time taken: {duration}s')
