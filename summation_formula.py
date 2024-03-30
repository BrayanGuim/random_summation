#we want to create a software that solves the following summation: (2**k)*(k**2), where k=0 is the starting point and n the final point.
#we will want to return f(n)*mod m since the result may be large
def f(n) : 
    if (2<=n <=10**18):
        for n in range(0,n,1):
            sum1 = []
            sum_formula = (2**n)*(n**2)
            sum1.append(sum_formula) 
        m = 10^9 + 7
        module = sum(sum1) % m
        print(f'f(n): {sum(sum1)}' )
        print(f'f(n) * mod m: {module}')
    else: 
        print('Value not in the domain of [2,10**18]')
f(int(input("n = ")))