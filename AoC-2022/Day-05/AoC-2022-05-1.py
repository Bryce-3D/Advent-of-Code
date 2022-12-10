#Retrieving the info
f = open('AoC-2022-05-Input.txt', 'r')
a = f.read().split('\n')
f.close()

#Blocks copied and removed from input file
'''
            [L] [M]         [M]    
        [D] [R] [Z]         [C] [L]
        [C] [S] [T] [G]     [V] [M]
[R]     [L] [Q] [B] [B]     [D] [F]
[H] [B] [G] [D] [Q] [Z]     [T] [J]
[M] [J] [H] [M] [P] [S] [V] [L] [N]
[P] [C] [N] [T] [S] [F] [R] [G] [Q]
[Z] [P] [S] [F] [F] [T] [N] [P] [W]
 1   2   3   4   5   6   7   8   9 
'''

#Manually encode the stacks
stack = [['Z','P','M','H','R'],
         ['P','C','J','B'],
         ['S','N','H','G','L','C','D'],
         ['F','T','M','D','Q','S','R','L'],
         ['F','S','P','Q','B','T','Z','M'],
         ['T','F','S','Z','B','G'],
         ['N','R','V'],
         ['P','G','L','T','D','V','C','M'],
         ['W','Q','N','J','F','M','L']]

for Homu in a:
    l = Homu.split(' ')
    n = int(l[1])      #Number of blocks to move
    i0 = int(l[3])-1   #From index
    i1 = int(l[5])-1   #To index

    #Perform the operation
    for Kumi in range(n):
        stack[i1].append(stack[i0].pop())

#Get the top of each stack
ans = [i[-1] for i in stack]
ans = ''.join(ans)
print(ans)
