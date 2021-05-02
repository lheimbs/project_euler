t = lambda n: n*(n+1)/2
p = lambda n: n*(3*n-1)/2
h = lambda n: n*(2*n-1)

it, ip, ih = 1,1,1
lt, lp, lh = t(it), p(ip), h(ih)
while True:
    while lp < lt:
        ip += 1
        lp = p(ip)
    while lh < lt:
        ih += 1
        lh = h(ih)
    if lh == lp and lp == lt:
        print(lt)
        if lt != 1 and lt != 40755:
            break
    it += 1
    lt = t(it)

