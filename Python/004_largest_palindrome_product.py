res = []
for i in reversed(range(1000)):
    for j in reversed(range(1000)):
        ress = i*j
        resstring = str(ress)
        if ress and resstring == "".join([ch for ch in reversed(resstring)]):
            res.append(ress)
print(max(res))
