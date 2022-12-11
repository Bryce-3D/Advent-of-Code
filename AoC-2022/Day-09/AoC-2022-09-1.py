#Retrieving the info
f = open('AoC-2022-09-Input.txt', 'r')
a = f.read().split('\n')
f.close()

#Vector for each direction
vec = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}

H = [0,0]   #Head
T = [0,0]   #Tail
seen = [[0,0]]   #Coords seen by T

for move in a:
    move = move.split()

    dir = move[0]
    n = int(move[1])

    for Homu in range(n):
        #Update the position of the head
        H[0] += vec[dir][0]
        H[1] += vec[dir][1]

        #Update the position of the tail if needed
        if abs(H[0]-T[0]) == 2:     #If too far horizontally 
            T[0] = (H[0]+T[0])//2
            T[1] = H[1]
        elif abs(H[1]-T[1]) == 2:   #Elif too far vertically
            T[1] = (H[1]+T[1])//2
            T[0] = H[0]
        
        #Update seen
        if T not in seen:
            seen.append([i for i in T])   #Unwrap to pass by val
    
print(len(seen))
