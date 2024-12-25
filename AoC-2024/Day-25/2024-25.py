def block_to_arr(block:str) -> list[int]:
    block = block.split('\n')
    R,C = len(block),len(block[0])
    #Start with -1 since the top/bot row doesn't count
    ans = [-1 for c in range(C)]
    for r in range(R):
        for c in range(C):
            if block[r][c] == '#':
                ans[c] += 1
    return ans

def fit(lock:list[int], key:list[int]) -> bool:
    l = len(lock)
    check = [lock[i]+key[i] for i in range(l)]
    return max(check) <= 5

def parse_input(fn:str) -> tuple[
    list[list[int]], list[list[int]]
]:
    with open(fn, 'r') as f:
        txt = f.read()
    locks_and_keys = txt.split('\n\n')

    locks,keys = [],[]

    for lock_or_key in locks_and_keys:
        arr_form = block_to_arr(lock_or_key)
        if lock_or_key[0][0] == '#':
            locks.append(arr_form)
        else:
            keys.append(arr_form)
    
    return locks,keys

def solve(fn:str) -> int:
    locks,keys = parse_input(fn)
    ans = 0
    for lock in locks:
        for key in keys:
            if fit(lock,key):
                ans += 1
    return ans

print(solve('Input.txt'))
