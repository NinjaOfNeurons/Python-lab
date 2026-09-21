def printN(count):

    if count == 4:
        return

    print(count)
    printN(count + 1)


printN(1)