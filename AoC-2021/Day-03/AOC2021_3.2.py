f = open('AOC2021_3_Input.txt', 'r')
l = {i for i in f.read().split('\n')}
f.close()

#Length of each binary string
k = len(l.pop())



#Finding the oxygen generator rating, aka the majority bit
a = l #List where we gradually eliminate strings
i = 0 #Track the position of the bit currently being analyzed

while len(a) != 1: #While there is more than 1 string
	#Check how many bits in position i are 0s or 1s
	c0 = 0
	c1 = 0
	for x in a:
		if x[i] == '0':
			c0 += 1
		elif x[i] == '1':
			c1 += 1
		else:
			print(f'Something\'s wrong with the element {x}')

	#Compare the 0 and 1 tallies and eliminate accordingly
	rem_a = set() #Set of stuff to remove
	if c0 <= c1:
		for x in a:
			if x[i] == '0':
				rem_a.add(x)
	elif c0 > c1:
		for x in a:
			if x[i] == '1':
				rem_a.add(x)
	a = a - rem_a

	#Update the bit position being analyzed
	i += 1

#Retrieving the remaining string
O2 = int(list(a)[0], 2)
print(f'Oxygen generator rating: {O2}')



#Finding the CO2 scrubber rating, aka the minority bit
b = l #List where we gradually eliminate strings
j = 0 #Track the position of the bit currently being analyzed

while len(b) != 1: #While there is more than 1 string
	#Check how many bits in position j are 0s or 1s
	c0 = 0
	c1 = 0
	for x in b:
		if x[j] == '0':
			c0 += 1
		elif x[j] == '1':
			c1 += 1
		else:
			print(f'Something\'s wrong with the element {x}')

	#Compare the 0 and 1 tallies and eliminate accordingly
	rem_b = set() #Set of stuff to remove
	if c0 <= c1:
		for x in b:
			if x[j] == '1':
				rem_b.add(x)
	elif c0 > c1:
		for x in b:
			if x[j] == '0':
				rem_b.add(x)
	b = b - rem_b

	#Update the bit position being analyzed
	j += 1

#Retrieving the remaining string
CO2 = int(list(b)[0], 2)
print(f'CO2 scrubber rating: {CO2}')

print(O2*CO2)






