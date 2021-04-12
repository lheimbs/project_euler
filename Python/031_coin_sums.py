
def combinations(iterable, goal, summ=0, combination=None):
#    print(summ, combination, id(sum), id(combination))

    if summ == goal:
        yield tuple(combination)
    elif summ > goal:
        return

    if not combination:
        for elem in iterable:
            combination = [elem]
            s = elem
            yield from combinations(iterable, goal, s, combination)
    else:
        for elem in iterable:
            if summ + elem > goal:
                continue
            s = summ + elem
            combi = combination[:]
            combi.append(elem)
            yield from combinations(iterable, goal, s, combi)


summs = set()
i = 0
for c in combinations([1,2,5,10,20,50,100,200], 200):
#    print(sum(c), c)#, end=", ")
    i += 1
    summs.add(tuple(sorted(c)))

print(len(summs), i)

