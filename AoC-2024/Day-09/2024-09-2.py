with open('Input.txt', 'r') as f:
    txt = f.read()

'''None of the files are empty'''
# for c in txt[::2]:
#     if c == '0':
#         print('empty file')

'''IDEA
The main issue is finding where to insert stuff
Keep track of indices of gaps of size n
Gaps are of size at most 9 (no files are empty)

hole_inds[i] = list of indices for a hole of size i

Place into hole -> die or become smaller hole
New smaller hole of size i created -> need to update hole_inds[i]

To make updating hole[i] faster
- Store hole[i] in reverse order (earliest hole at the end)
- Allows for faster appending
- Maybe insertion sort pushing it inwards (should be fast unless you get a 
  corner case of like a hole of size 1 being generated when you have like 
  5649098127754 holes of size 1 beforehand)
'''

def init_memory(s:str) -> list[int]:
    n = sum([int(i) for i in s])
    a = [None for i in range(n)]
    id,ind = 0,0
    for Homu in range(len(s)):
        k = int(s[Homu])
        #Empty space
        if Homu%2 == 1:
            ind += k
            continue
        #Write the file id
        for i in range(k):
            a[ind] = id
            ind += 1
        #Increment to next file id
        id += 1
    return a

def init_hole_inds(s:str) -> list[list[int]]:
    '''
    hole_inds[i] = list of indices of holes of size n of size i
                   in reverse order
    '''
    ans = [[] for i in range(10)]
    ans[0] = None   #Don't record holes of size 0
    
    ind = 0                       #Pointer to memory position
    for i in range(len(s)):
        k = int(s[i])             #Get the size
        if i%2 != 0 and k != 0:   #If non-trivial free space
            ans[k].append(ind)    #Apend to list
        ind += k                  #Update pointer

    #Reverse the order of the indices
    for i in range(1,10):
        ans[i] = ans[i][::-1]
    
    return ans

def init_og_file_inds(s:str) -> list[int]:
    '''Get the indices of the start of each file originally'''
    ans = []
    ind = 0
    for i in range(len(s)):
        if i%2 == 0:          #If a file
            ans.append(ind)   #Record the index
        ind += int(s[i])      #Update memory pointer
    return ans

n = len(txt)//2 + 1   #Number of files
a = init_memory(txt)
hole_inds = init_hole_inds(txt)
og_file_inds = init_og_file_inds(txt)



outside = len(a)+21   #Index to mark far out to the right
for file_id in range(n-1,-1,-1):
    #Get the size and location of the kth file
    file_sz = int(txt[2*file_id])
    og_ind = og_file_inds[file_id]

    #DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # print(file_sz)
    # print(og_ind)
    #DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #Find the leftmost possible hole to slot it in, if any
    leftmost_ind = outside   #Initialize to large value
    hole_sz = None
    for i in range(file_sz,10):
        #Skip if there are no holes of size i
        if len(hole_inds[i]) == 0:
            continue
        #Get leftmost hole of size i
        ind = hole_inds[i][-1]
        #If further left and to left of file, then update the leftmost hole
        if ind < og_ind and ind < leftmost_ind:
            leftmost_ind = ind
            hole_sz = i
    
    #No hole to the left is big enough, skip
    if leftmost_ind == outside:
        continue

    #If hole found, then move the file
    for i in range(file_sz):
        a[leftmost_ind+i] = file_id
        a[og_ind+i] = None

    #and update hole_inds
    hole_inds[hole_sz].pop()
    new_hole_size = hole_sz - file_sz
    if new_hole_size != 0:
        #Get the list of indices of the relevant size
        l = hole_inds[new_hole_size]
        new_ind = leftmost_ind + file_sz
        l.append(new_ind)
        #Remember to sort the inds in descending order
        #Sort by using insertion sort to slide in the new index
        k = len(l)-1
        while k > 0 and l[k-1] < l[k]:
            l[k-1],l[k] = l[k],l[k-1]
            k -= 1



#Calcualte the answer
ans = 0
for i in range(len(a)):
    if a[i] != None:
        ans += i*a[i]
print(ans)
