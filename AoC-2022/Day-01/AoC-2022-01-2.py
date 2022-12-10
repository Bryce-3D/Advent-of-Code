#Retrieving the info
f = open('AoC-2022-01-Input.txt', 'r')
l = f.read().split('\n')
f.close()

top = []
curr = 0
for val in l:
    if val == '':   #If divider
        #Append curr then reset it
        top.append(curr)
        curr = 0

        #Sort in descending order then pop the smallest 
        #if there's more than 3 already
        top.sort(key = lambda x: -x)
        if len(top) > 3:
            top.pop()

    else:   #If next value
        curr += int(val)

print(sum(top))
