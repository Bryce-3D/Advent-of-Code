with open('Input.txt', 'r') as f:
    txt = f.read()

def single_update(n:int) -> list[int]:
    if n == 0:
        return [1]
    if len(str(n))%2 == 0:
        s = str(n)
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        return [int(a),int(b)]
    return [2024*n]

#Store the stones as num:freq pairs instead
def row_dict_update(stones:dict[int,int]) -> dict[int,int]:
    ans = {}
    for n in stones:
        for k in single_update(n):
            if k in ans:
                ans[k] += stones[n]
            else:
                ans[k] = stones[n]
    return ans

def solve(stones:list[int], rounds:int) -> int:
    #Convert from a list to a dict
    d = {}
    for n in stones:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    #Update the dict `rounds` times
    for i in range(rounds):
        d = row_dict_update(d)
    #Get the total number of stones
    ans = 0
    for n in d:
        ans += d[n]
    return ans

stones = [int(i) for i in txt.split()]
print(solve(stones, 25))
print(solve(stones, 75))





#Recyclling Bin ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def row_update(stones:list[int]) -> list[int]:
    ans = []
    for n in stones:
        for k in single_update(n):
            ans.append(k)
    return ans
