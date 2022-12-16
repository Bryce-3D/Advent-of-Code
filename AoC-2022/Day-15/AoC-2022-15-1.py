#Retrieving the info
f = open('AoC-2022-15-Input.txt', 'r')
inp = f.read().split('\n')
f.close()

#Note to self: some beacons lie on y = 2x10^6

#Parsing the input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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



#Actually solving the problem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Y = 2000000
#Set of x-coords along y=Y that cannot have a beacon
blocked = set()

for pair in pairs:
    #Get dist between the sensor and nearest beacon
    sen = pair[0]
    bea = pair[1]
    dist = abs(sen[0]-bea[0]) + abs(sen[1]-bea[1])
    dist_y = abs(sen[1]-Y)   #How far the sensor is from the line y=Y
    dist_x = dist - dist_y   #How far the sensor covers horizontally outwards

    min_x = sen[0] - dist_x
    max_x = sen[0] + dist_x
    for i in range(min_x, max_x+1):
        blocked.add(i)
    
    #Corner case where the beacon lies on y=Y
    if bea[1] == Y:
        blocked.remove(bea[0])   #Remove it from `blocked`

print(len(blocked))
