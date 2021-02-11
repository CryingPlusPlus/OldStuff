
def solver(n):
    for e in range(1, n):
        for b in range(1, n):
            for z in range(1, n):
                for h in range(3, n):
                    if e**h+b**h == z**h:
                        print('e:', e, 'h:', h, 'z:', z,'b:', b)
                        return


solver(100)