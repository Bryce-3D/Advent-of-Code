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

    #If there's an overlap, increase ans
    if end[0][0] <= end[1][1] and end[0][1] >= end[1][0]:
        ans += 1

print(ans)
