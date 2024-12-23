from collections import defaultdict

def parse_input(fn:str) -> dict[str,set[str]]:
    with open(fn, 'r') as f:
        txt = f.read()
    edges = [
        line.split('-')
        for line in txt.split('\n')
    ]
    ans = defaultdict(set)
    for edge in edges:
        v0,v1 = edge
        ans[v0].add(v1)
        ans[v1].add(v0)
    return ans

def part_1(adj_list:dict[str,set[str]]) -> int:
    ans = 0
    #For each pair of vertices
    for v0 in adj_list:
        for v1 in adj_list:
            #Check neighbors
            neigh0 = adj_list[v0]
            neigh1 = adj_list[v1]
            #Not connected -> Insta skip
            if v1 not in neigh0:
                continue
            #Get common neighbors
            for neigh in neigh0:
                if neigh not in neigh1:
                    continue
                #Check if 't' is part of the trio
                if 't' in [v0[0], v1[0], neigh[0]]:
                    ans += 1
    #Account for the 6x count
    if ans%6 != 0:
        raise Exception(f'What ({ans} is not div by 6)')
    return ans//6

adj_list = parse_input('Input.txt')
print(part_1(adj_list))
