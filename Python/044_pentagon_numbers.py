#import utils
#from tqdm import tqdm

p = lambda n: int(n*(3*n-1)/2)

MAX=int(10e6)
ps = {i: p(i) for i in range(1, MAX)}

j = 1
D = 10e100
while j < 10e10:
    print(j, end='\r')
    pj = p(j)
    for k in range(j+1, MAX):
        pk = p(k)
        while pj+pk > max(ps.values()):
            ps |= {i: p(i) for i in range(MAX, MAX*10)}
            MAX *= 10
        if pj+pk in ps.values() and pj-pk in ps.values() and abs(pk-pj) < D:
            D = abs(pk-pj)
            print(pj, pk, D)
    j += 1

