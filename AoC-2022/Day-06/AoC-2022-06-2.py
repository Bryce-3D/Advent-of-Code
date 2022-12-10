#Retrieving the info
f = open('AoC-2022-06-Input.txt', 'r')
s = f.read()
f.close()

ans = 0
end = []
for c in s:
    ans += 1

    #Updating end
    if len(end) < 14:
        end.append(c)
    else:
        end.pop(0)
        end.append(c)
    
    #Checking if 14 distinct characters exist
    end_set = {i for i in end}
    if len(end_set) == 14:
        break

print(ans)
