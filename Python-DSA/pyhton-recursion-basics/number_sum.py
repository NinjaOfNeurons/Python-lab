def printN(count, sum_n):

    if count == 4:
        print("Sum:", sum_n)
        return

    print(count)
    sum_n = sum_n + count

    printN(count + 1, sum_n)


printN(1, 0)