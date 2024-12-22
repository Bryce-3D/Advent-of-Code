'''IDEA
16777216 = 2**24
'''

PRUNE = (1 << 24) - 1

def update(n:int) -> int:
    n = ((n <<  6) ^ n) & PRUNE
    n = ((n >>  5) ^ n) & PRUNE
    n = ((n << 11) ^ n) & PRUNE
    return n

def sell(n:int, iter:int=2000) -> dict[tuple[int,int,int,int],int]:
    '''
    Given a starting price n, returns a dictionary 
    where each key-value pair is of the form
        tuple of prices to watch for : sell value
    If a tuple of prices does not appear, then it 
    will not appear as a key in the dictionary
    '''

with open('Input.txt', 'r') as f:
    txt = f.read()
a = [int(i) for i in txt.split('\n')]

ans = 0
for n in a:
    for i in range(2000):
        n = update(n)
    ans += n
print(ans)
