def fibo (x):
    a=0
    b=1
    for i in range(x):
        c=a+b
        a=b
        b=c
        print (c, end = " ")
fibo(10)