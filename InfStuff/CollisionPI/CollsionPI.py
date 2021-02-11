

def pi():

    bigX = 0
    bigM = 10000000000
    bigV = -1

    smolX = -100
    smolW = 10
    smolM = 1
    smolV = 0

    c = 0
    run = 0
    while run == 0:
        #print(c)
        if bigV >= 0:
            if abs(smolV) <= abs(bigV):
                if smolV >= 0:
                    run = 1

        bigX = bigX + bigV
        smolX = smolX + smolV

        if smolX + smolW > bigX:
            c = c + 1
            sumM = bigM + smolM
            bV = (bigM - smolM)/sumM * bigV + 2 * smolM/sumM * smolV
            sV = 2 * bigM/sumM * bigV + (smolM - bigM)/sumM * smolV

            bigV = bV
            smolV = sV
        if smolX < -150:
            c = c + 1
            smolV = smolV * -1
    return c
print(pi())