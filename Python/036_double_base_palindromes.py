import utils

N = utils.get_N() if utils.get_N() else int(1e6)

finds = []
for i in range(1, N):
    if utils.is_palindrome(i):
        i_bin = bin(i)[2:]
        if utils.is_palindrome(i_bin):
            finds.append(i)

assert 585 in finds
print(finds)
print(sum(finds))

