#Retrieving the info
f = open('AoC-2022-02-Input.txt', 'r')
l = f.read().split('\n')
f.close()

'''
A = Roc 1pt
B = Pap 2pt
C = Sci 3pt

X = lose 0pt
Y = draw 3pt
Z = win  6pt
'''

#pts[game] = number of points you earn when the game 'game' happens
#Ex: pts['A X'] = 0 (lose) + 3 (scissors) = 4
pts = {'A X': 0+3, 'A Y': 3+1, 'A Z': 6+2,
       'B X': 0+1, 'B Y': 3+2, 'B Z': 6+3,
       'C X': 0+2, 'C Y': 3+3, 'C Z': 6+1}

#Remove the empty string at the end
l.pop()

score = 0
for game in l:
    score += pts[game]
print(score)
