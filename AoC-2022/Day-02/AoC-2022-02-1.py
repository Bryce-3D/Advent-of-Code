#Retrieving the info
f = open('AoC-2022-02-Input.txt', 'r')
l = f.read().split('\n')
f.close()

'''
Anti-you  You
   A       X   1pt Rock
   B       Y   2pt Paper
   C       Z   3pt Scissors
'''

#pts[game] = number of points you earn when the game 'game' happens
#Ex: pts['A X'] = 3 (draw) + 1 (rock) = 4
pts = {'A X': 3+1, 'A Y': 6+2, 'A Z': 0+3,
       'B X': 0+1, 'B Y': 3+2, 'B Z': 6+3,
       'C X': 6+1, 'C Y': 0+2, 'C Z': 3+3}

#Remove the empty string at the end
l.pop()

score = 0
for game in l:
    score += pts[game]
print(score)
