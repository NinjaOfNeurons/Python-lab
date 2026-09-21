def fibo(n,n1,n2,count):
    if n == 0:
        print(0)
        return
    elif n==1:
        print(0,1)
        return 
    if count <= n:
        nth = n1+n2
        print(n1)
        fibo(n, n1=n2,n2=nth,count= count+1)


print(fibo(1,0,1,0))