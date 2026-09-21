def factorial(count, fact):
    if(count == 1):
        print(fact)
        return
    fact = fact * count
    factorial(count - 1, fact)


factorial(count=4, fact=1)