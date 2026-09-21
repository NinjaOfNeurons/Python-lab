def perfect_num(num):
    sum = 0
    for i in range(1, num):
        

        if(num % i == 0):
            sum  = sum + i
            print(i,sum)
    return sum == num



print(perfect_num(1176))        
