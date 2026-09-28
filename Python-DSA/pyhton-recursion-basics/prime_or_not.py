def chk_prime(i, n):
    if(i == n):
        return True
    if(n%i == 0):
        return False
    # print(i)
    return chk_prime(i+1, n)

print(chk_prime(i=2, n=5))