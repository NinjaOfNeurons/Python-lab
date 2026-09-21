def sum_first_n(count,sum_1):
    if count == 1:
        print(sum_1)
        return 
    sum_1 = sum_1 + count

    # print(sum)
    
    sum_first_n(count - 1,sum_1)






sum_first_n(5,1)