def nto1(count):
    if count == 1:
        return

    print(count)
    nto1(count - 1)

n = 5
nto1(n)