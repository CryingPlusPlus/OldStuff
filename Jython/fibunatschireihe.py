def fibreihe(k): 
    for k in range(k): 
        print (fib(k)) 
        
def fib(i):
    if i<=2: 
        return 1
    else: 
        return fib(i-1)+fib(i-2)
        
fibreihe(4)