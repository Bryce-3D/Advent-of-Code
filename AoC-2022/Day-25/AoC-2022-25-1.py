#Retrieving the info
f = open('AoC-2022-25-Input.txt', 'r')
inp = f.read().split('\n')
f.close()

#Store the value of each char and vice versa
val = {'=':-2, '-':-1, '0':0, '1':1, '2':2}
sym = {-2:'=', -1:'-', 0:'0', 1:'1', 2:'2'}

#Turns a string rep of a SNAFU to an int
def un_SNAFU(SNAFU):
    l = len(SNAFU)
    ans = 0
    
    for i in range(l):
        c = SNAFU[-i-1]
        v = val[c] * (5**i)
        ans += v
    
    return ans

#Turns an int to a string rep of a SNAFU
#Only works for positive integer values
'''Idea
Note that the last digit is uniquely determined by 
the mod 5 of the number. Use mod 5 to get the last 
digit, then recursively find the next rightmost digit.
'''
def re_SNAFU(dec):
    ans = []
    while dec != 0:
        r = dec%5
        if r > 2:
            r -= 5
        ans.append(sym[r])
        dec = (dec - r)//5
    ans = ans[::-1]
    ans = ''.join(ans)
    return ans



ans = 0
for SNAFU in inp:
    ans += un_SNAFU(SNAFU)
ans = re_SNAFU(ans)
print(ans)
