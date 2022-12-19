#Retrieving the info
f = open('AOC2021_2_Input.txt', 'r')
l = f.read().split('\n')
f.close()

#Test case
#l = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']

hor = 0
dep = 0
aim = 0

n = len(l)
for i in range(n):
	if l[i][0] == 'f':
		k = int(l[i][-1])
		hor += k
		dep += aim * k
	elif l[i][0] == 'd':
		aim += int(l[i][-1])
	elif l[i][0] == 'u':
		aim -= int(l[i][-1])

print(hor)
print(dep)
print(hor*dep)
