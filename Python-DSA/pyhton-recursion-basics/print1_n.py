def print_1_to_n(count,n):
    if count == n+1:
        return
    print(count)

    print_1_to_n(count + 1 , n)


print_1_to_n(count=1, n=5)