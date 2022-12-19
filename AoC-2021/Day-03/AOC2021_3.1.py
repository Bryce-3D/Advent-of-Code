f = open('AOC2021_3_Input.txt', 'r')
l = f.read().split('\n')
f.close()

#l = ['111000','101010','110010','100101','001101']

#n is the length of the list, k is the length of each binary string
n = len(l)
k = len(l[0])
#List of bits of gamma
l_gam = []

print(f'n is {n} and k is {k}')

print(l[999][0])

#For each place value
for i in range(k):
	#c0 and c1 count the number of 0s and 1s in each place resp
	c0 = 0
	c1 = 0

	for j in range(n):
		#print(j) #DEBUG
		if l[j][i] == '0':
			c0 += 1
		elif l[j][i] == '1':
			c1 += 1
		else:
			print(f'Typo at line {j}')

	if c0 > c1:
		l_gam.append(0)
	elif c1 > c0:
		l_gam.append(1)
	else:
		print('c0=c1?')


#Numerical alue of gamma
gam = 0

for i in range(k):
	gam = 2*gam + l_gam[i]

eps = 2**k-1 - gam

print(l_gam)
print(gam*eps)
