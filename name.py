def f(a):
    if(n<=1):
        return a
    else:
        return (f(n-1)+f(n-2))
a=int(raw_input())
for i in range(1,n+1):
    print f(i),
