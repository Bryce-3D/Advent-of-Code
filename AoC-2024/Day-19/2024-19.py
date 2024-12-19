'''IDEA
Just use DP with memoization
'''

from functools import cache

@cache
def is_possible(towels:tuple[str,...], design:str) -> bool:
    #Fully matched
    if design == '':
        return True
    for towel in towels:
        #Towel too long
        if len(towel) > len(design):
            continue
        #Towel does not match prefix
        if towel != design[:len(towel)]:
            continue
        #If towel matches prefix, check if rest works
        if is_possible(towels, design[len(towel):]):
            return True
    #Impossible
    return False

@cache
def num_ways(towels:tuple[str,...], design:str) -> int:
    #Fully matched
    if design == '':
        return 1
    ans = 0
    for towel in towels:
        #Towel too long
        if len(towel) > len(design):
            continue
        #Towel does not match prefix
        if towel != design[:len(towel)]:
            continue
        #If towel matches prefix, check number of ways for the rest
        ans += num_ways(towels, design[len(towel):])
    return ans



with open('Input.txt', 'r') as f:
    txt = f.read()

towels, designs = txt.split('\n\n')
towels = tuple(i.strip() for i in towels.split(','))
designs = designs.split()

ans = 0
for design in designs:
    if is_possible(towels, design):
        ans += 1
print(ans)

ans = 0
for design in designs:
    ans += num_ways(towels, design)
print(ans)
