with open('Input.txt', 'r') as f:
    txt = f.read()

def score(M:list[list[int]], r0:int, c0:int) -> int:
    if M[r0][c0] != 0:
        return 0
    
    R,C = len(M),len(M[0])

    #BFS[i] = list of reachable positions of height i
    BFS = [[] for i in range(10)]
    BFS[0] = [[r0,c0]]
    for h in range(9):
        frontier = BFS[h]
        for node in frontier:
            r,c = node
            neighs = [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]
            for neigh in neighs:
                r_,c_ = neigh
                if 0 <= r_ < R and 0 <= c_ < C and M[r_][c_] == h+1:
                    if [r_,c_] not in BFS[h+1]:
                        BFS[h+1].append([r_,c_])
    return len(BFS[9])



M = [[int(i) for i in row] for row in txt.split('\n')]
R,C = len(M),len(M[0])

ans = 0
for r in range(R):
    for c in range(C):
        ans += score(M,r,c)
print(ans)
