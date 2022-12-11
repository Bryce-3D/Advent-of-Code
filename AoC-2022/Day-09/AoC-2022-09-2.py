#Retrieving the info
f = open('AoC-2022-09-Input.txt', 'r')
a = f.read().split('\n')
f.close()

'''Idea
Can prove by induction that every segment moves at most 1 unit in 
each direction at every step and that a movement occurs iff the 
next segment is exactly 2 units away in at least one direction.

Suppose ith moves at most 1 unit in each direction.
(i+1)th was originally touching the ith segment.
Therefore, the (i+1)th is at most 2 units away in each direction.
The worst case is
    ..A    ..A
    ... => .B.
    B..    ...
in which the (i+1)th segment moves one unit in each direction.
Every other case has been defined in part 1 of the problem, and 
they also all don't move it more than 1 unit in either direction.

Also note that dist on both directions <= 1 -> adjacent.
Also dist in a direction is <= 2.
So not adj iff dist in a direction = 2.
'''

#Vector for each direction
vec = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}

#rope[i] = coord of ith segment of rope
rope = [[0,0] for i in range(10)]
seen = [[0,0]]   #Coords seen by 9th segment

for move in a:
    move = move.split()

    dir = move[0]
    n = int(move[1])

    for Homu in range(n):
        #Update the position of the head
        rope[0][0] += vec[dir][0]
        rope[0][1] += vec[dir][1]

        #Update the position of the (i+1)-th segment
        for i in range(9):
            delta_x = abs(rope[i+1][0] - rope[i][0])   #Horizontal dist
            delta_y = abs(rope[i+1][1] - rope[i][1])   #Vertical dist
            
            if delta_x == 2 and delta_y == 2:   #If too far both ways
                rope[i+1][0] = (rope[i][0] + rope[i+1][0])//2
                rope[i+1][1] = (rope[i][1] + rope[i+1][1])//2
            elif delta_x == 2:                  #Elif too far horizontally only
                rope[i+1][0] = (rope[i][0] + rope[i+1][0])//2
                rope[i+1][1] = rope[i][1]
            elif delta_y == 2:                  #Elif too far vertically only
                rope[i+1][0] = rope[i][0]
                rope[i+1][1] = (rope[i][1] + rope[i+1][1])//2
            #Else they are adjacent 
        
        #Update seen
        if rope[9] not in seen:
            seen.append([i for i in rope[9]])   #Unwrap to pass by val
    
print(len(seen))
