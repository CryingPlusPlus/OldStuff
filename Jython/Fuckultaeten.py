def f(i): 
    if i < 2:
        return 1 
    else: 
        return i*f(i-1)
print (f(12))