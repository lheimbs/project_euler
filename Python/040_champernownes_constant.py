import utils

def get_cham_str(max_len):
    cham_str = ""
    i = 0
    while len(cham_str) <= max_len:
        cham_str += str(i)
        i += 1
    return cham_str



N = utils.get_N() if utils.get_N() else 6
MAX = int(10**N)
print(MAX)
cham_str = get_cham_str(MAX)

cons = 1
for i in range(1, N+1):
    print(10**i, cham_str[10**i])
    cons *= int(cham_str[10**i])
print(cons)

