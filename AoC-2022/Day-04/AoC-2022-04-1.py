#Retrieving the info
f = open('AoC-2022-04-Input.txt', 'r')
a = f.read().split('\n')
f.close()

ans = 0

for Homu in a:
    #Split it up by ',' then by '-'
    end = [i.split('-') for i in Homu.split(',')]
    #Cast to int
    end = [[int(i) for i in j] for j in end]

    #If end[0] is contained within end[1]
    if end[0][0] >= end[1][0] and end[0][1] <= end[1][1]:
        ans += 1
    #If end[1] is contained within end[0]
    elif end[1][0] >= end[0][0] and end[1][1] <= end[0][1]:
        ans += 1

print(ans)
