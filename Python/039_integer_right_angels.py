from tqdm import tqdm
MAX = 1000
max_res = (0, 0)
for p in tqdm(range(10, MAX+1)):
    ress = 0
    for i in range(1,p):
        for j in range(i, p):
            k = p - i - j
            if k > 0 and i**2+j**2 == k**2:
                ress += 1
    if ress > max_res[1]:
        max_res = (p, ress)
print(max_res)
