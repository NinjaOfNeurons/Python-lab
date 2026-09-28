def str_rotation(start, stop, stringh):
    i = start
    j = stop
    while(i<j):
        stringh[i] ,stringh[j] = stringh[j], stringh[i]
        i += 1
        j -= 1
    return stringh






stringh = "abcde"
stringh = list(stringh)
goal = "cdeab"
goal = list(goal)

k = 2
count= 0 

for i in range(len(stringh)):
    
    print(str_rotation(0,len(stringh)-1,stringh  ))
    print(str_rotation(0, k-1, stringh))
    print(str_rotation(k, len(stringh)-1, stringh))
    count += 1

    if stringh == goal:
        print("yeah", count)
        break

    
stringh = "".join(stringh)
print(stringh)
    

