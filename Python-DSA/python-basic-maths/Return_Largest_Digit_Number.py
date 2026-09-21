def largest_num(num):
    largest = 0
    while(num != 0):
        current = num % 10
        if current > largest:
            largest = current
        num = num // 10
    return largest

print(largest_num(10))