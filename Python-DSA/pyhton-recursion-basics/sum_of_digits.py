#redo it by your own
def sum_dig(num, total):
    if(num==0):
        if(total<=9):
            print(total)
            return
        num = total
        total = 0
        
    last_digit  =  num % 10

    total = total + last_digit

    num  = num // 10

    # print("cz",total, last_digit,num)

    sum_dig(num, total)

sum_dig(529, 0)