def isprime(num):
    if(num == 2):
        return True
    for i in range(2, num):
        if(num % i == 0):
            return False
        else:
            return True

def prime_till_n(num):
    primes =[1]
    for i in range(1,num):
        if(isprime(i)):
            primes.append(i)
    return primes





print(prime_till_n(130))
