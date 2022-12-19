#Retrieving the info
f = open('AOC2021_2_Input.txt', 'r')
l = f.read().split('\n')
f.close()

hor = 0
dep = 0

n = len(l)
for i in range(n):
	if l[i][0] == 'f':
		hor += int(l[i][-1])
	elif l[i][0] == 'd':
		dep += int(l[i][-1])
	else:
		dep -= int(l[i][-1])

print(hor)
print(dep)
print(hor*dep)
