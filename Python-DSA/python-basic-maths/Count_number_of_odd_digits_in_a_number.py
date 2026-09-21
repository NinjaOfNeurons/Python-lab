def countOdd(num):
    count = 0
    while( num != 0):
        lastdigit = num % 10 
        if(lastdigit % 2 != 0):
            count += 1
        num = num // 10
    return count    

    



print(countOdd(210))