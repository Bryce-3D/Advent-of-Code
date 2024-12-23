'''IDEA
16777216 = 2**24
'''

PRUNE = (1 << 24) - 1

def update(n:int) -> int:
    n = ((n <<  6) ^ n) & PRUNE
    n = ((n >>  5) ^ n) & PRUNE
    n = ((n << 11) ^ n) & PRUNE
    return n

def part_1(a:list[int]) -> int:
    ans = 0
    for n in a:
        for i in range(2000):
            n = update(n)
        ans += n
    return ans

def sell(n:int, iter:int=2000) -> dict[tuple[int,int,int,int],int]:
    '''
    Given a starting price n, returns a dictionary 
    where each key-value pair is of the form
        tuple of prices to watch for : sell value
    If a tuple of prices does not appear, then it 
    will not appear as a key in the dictionary
    '''
    ans = {}
    deltas = []

    for Homu in range(iter):
        #Generate next price and record price change
        nex = update(n)
        deltas.append(nex%10 - n%10)
        n = nex
        #Not enough price changes yet
        if len(deltas) < 4:
            continue
        instr = tuple(deltas[-4:])
        #Already occurred
        if instr in ans:
            continue
        #First occurrence -> Record sell price
        ans[instr] = n%10
    
    return ans

def part_2(a:list[int]) -> int:
    #profit[instr] = number of bananas earned by the instruction
    profit = {}
    #For each seed
    for n in a:
        #Get the profit of all possible instructions
        indiv_profit = sell(n)
        #And add it to the totals
        for instr in indiv_profit:
            if instr in profit:
                profit[instr] += indiv_profit[instr]
            else:
                profit[instr] = indiv_profit[instr]
    #Then get the max possible profit
    ans = 0
    for instr in profit:
        ans = max(profit[instr], ans)
    return ans



with open('Input.txt', 'r') as f:
    txt = f.read()
a = [int(i) for i in txt.split('\n')]

print(part_1(a))
print(part_2(a))
