#For compressing for some loops together using itertools.product()
import itertools

f = open('AOC2021_4_Input.txt', 'r')
l = f.read().split('\n')
f.close()

#Testing purposes
#l = ['2 3 4 5 1 6 9 8 7', '', 
#'1 2 3 4 5', '6 7 8 9 10', '1 2 3 4 5', '1 2 3 4 5', '1 2 3 4 5', '',
#'2 3 4 1 2', '2 1 3 4 5', '2 3 4 5 1', '2 4 3 5 1', '2 4 3 5 6']

#n is the number of boards
n = len(l)
n = (n-1)//6

#List of numbers drawn in order
draws = l[0].split(',')

#List of all the boards, where each element of the list is a list of 5 lists of 5 numbers
#When a number is ticked, it will be changed to `X` to record the ticking
boards = [0 for i in range(n)]
for i in range(n):
	board_i = [0 for j in range(5)]
	for j in range(5):
		board_i[j] = l[6*i + 2 + j].split()
	boards[i] = board_i

#List of all tick counters for each board, where the ith element tracks the ticks for the ith board
#Each element of the form [[r0,r1,r2,r3,r4],[c0,c1,c2,c3,c4]]
#where ri and ci are the number of ticked elements of the ith row and ith column
ticks = [ [[0 for i in range(5)] for j in range(2)] for k in range(n) ]

#Finding the board that wins last
won = set() #Set of boards that have won
i = 0 #Index of number currently being drawn
check = 0 #Check if the last board has been found
while check == 0:
	draw = draws[i] #Number currently drawn
	#Loop through the element in row r and column c of board j
	for j, r, c in itertools.product(range(n), range(5), range(5)):
		if boards[j][r][c] == draw:
			boards[j][r][c] = 'X' #Tick the drawn number in the board
			ticks[j][0][r] += 1 #Increase corresponding row tick
			ticks[j][1][c] += 1 #Increase corresponding column tick
		if ticks[j][0][r] == 5 or ticks[j][1][c] == 5: #Completed row or column
			won.add(j)
			if check == 0 and len(won) == n: #check == 0 to not use other boards after getting the last board
				check = 1
				i_last = j
				last_draw = int(draw)

	#Proceed to the next draw if not every board won yet
	i += 1

#Getting the total of the unticked numbers of board i_last
total = 0
for r, c in itertools.product(range(5), range(5)):
	if boards[i_last][r][c] != 'X':
		total += int(boards[i_last][r][c])

print(i_last) #15
print(last_draw) #77
print(total) #784
print(total * last_draw) #60368
