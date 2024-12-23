import time
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

def get_K3(adj_list:dict[str,set[str]]) -> set[tuple[int,int,int]]:
    ans = set()
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
                if neigh in neigh1:
                    tri = sorted([v0,v1,neigh])
                    ans.add(tuple(tri))
    return ans

def get_Knext(adj_list:dict[str,set[str]], 
            Kns:set[tuple[int,...]]
            ) -> set[tuple[int,...]]:
    '''
    Given an adjacency list and the set of all n-cliques, 
    returns the set of all (n+1)-cliques.
    '''
    ans = set()
    for Kn in Kns:
        for v_new in adj_list:
            works = True
            for v in Kn:
                if v_new not in adj_list[v]:
                    works = False
                    break
            if works:
                K_new = list(Kn)
                K_new.append(v_new)
                K_new.sort()
                K_new = tuple(K_new)
                ans.add(K_new)
    return ans

def part_2_testing(adj_list:dict[str,set[str]]):
    '''It peaks at 6-cliques, likely brute forcable this way'''
    K3s = get_K3(adj_list)
    print(len(K3s))   #11011
    K4s = get_Knext(adj_list, K3s)
    print(len(K4s))   #26455
    K5s = get_Knext(adj_list, K4s)
    print(len(K5s))   #45045
    K6s = get_Knext(adj_list, K5s)
    print(len(K6s))   #55770
    K7s = get_Knext(adj_list, K6s)
    print(len(K7s))   #50622
    K8s = get_Knext(adj_list, K7s)
    print(len(K8s))   #33462

def part_2(adj_list:dict[str,set[str]]) -> set[tuple[int,...]]:
    Kns = get_K3(adj_list)
    Knexts = get_Knext(adj_list, Kns)
    while len(Knexts) > 0:
        Kns = Knexts
        Knexts = get_Knext(adj_list, Kns)
    return Kns

def part_2_parsed(adj_list:dict[str,set[str]]) -> list[str]:
    Kns = part_2(adj_list)
    ans = []
    for Kn in Kns:
        a = sorted(list(Kn))
        s = ','.join(a)
        ans.append(s)
    return ans

adj_list = parse_input('Input.txt')
t0 = time.time()
print(part_1(adj_list))
print(part_2_parsed(adj_list))
t1 = time.time()
print(f'{t1-t0} seconds taken')   #6.934496164321899 seconds taken
