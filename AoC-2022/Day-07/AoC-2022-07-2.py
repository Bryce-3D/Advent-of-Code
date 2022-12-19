#Retrieving the info
f = open('AoC-2022-07-Input.txt', 'r')
terminal = f.read().split('\n')
f.close()

'''Idea
Use a dictionary to represent each directory

Each item within a directory will be stored as a 
key value pair of the form 
    name, size        if it is a file
    name, directory   if it is a directory

Maybe use a stack to be able to backtrack (cd ..) 
pop() when going back a directory
push() when going into a directory
Current directory is the one on top

Then for getting the sizes, a recursive function 
will probably work
    Argument is an int
        Return the int itself
    Argument is a dict
        Return sum(f(values))
'''

#Process the input
root = {}
curr = [root]   #Stack of where we are atm

i = 0   #Line number of terminal currently looked at
l = len(terminal)

while i < l:
    line = terminal[i].split()

    #Debug jic
    #The start of any iteration of the while loop should contain 
    #a terminal command. If the `ls` command is seen, the iteration 
    #should run through all listed files and increment i to reach 
    #the next command.
    if line[0] != '$':
        print(f'Something broke at line {i}')

    if line[1] == 'cd':
        if line[2] == '/':
            curr = [root]
        elif line[2] == '..':
            curr.pop()   #Go out one directory
        else:
            name = line[2]
            dest = curr[-1][name]
            curr.append(dest)
    
    elif line[1] == 'ls':
        #While next line is not a dir, go down and encode it
        while i < l-1 and terminal[i+1][0] != '$':
            i += 1
            content = terminal[i].split()
            name = content[1]

            if content[0] == 'dir':
                curr[-1][name] = {}   #Initialize an empty folder
            else:
                size = int(content[0])
                curr[-1][name] = size   #Record file size
    
    i += 1



#Finding the ans
#Given a dict/int representing a dir/file, returns the size
def size_of(dir):
    if isinstance(dir, int):
        return dir
    
    ans = 0
    for name in dir:
        ans += size_of(dir[name])

    return ans

used = size_of(root)   #Total amount of used capacity


ans = 70000000
remove = 30000000 - (70000000 - used)   #Min amount to remove
#Takes in a dict or int representing a dir or file
#if dir:
#    Calculates the size
#    if size >= remove
#        ans = min(size, ans)
#    return size
#if file:
#    return size
def check(dir):
    global ans

    if isinstance(dir, int):
        return dir
    
    size = 0
    for name in dir:
        size += check(dir[name])
    
    if size >= remove:
        ans = min(size, ans)
    
    return size

check(root)
print(ans)
