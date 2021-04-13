
def combinations(iterable, goal, summ=0, combination=None, latest=None):
#    print(summ, combination, iterable)

    if summ == goal:
        yield tuple(combination)
    elif summ > goal:
        return

    if not combination:
        for elem in iterable:
            combination = [elem]
            s = elem
            yield from combinations(iterable, goal, s, combination, elem)
    else:
        if not iterable:
            return
        if latest is not None:
            iterable = iterable[iterable.index(latest):]

        for elem in iterable:
            if summ + elem > goal:
                continue
            s = summ + elem
            combi = combination[:]
            combi.append(elem)
            yield from combinations(iterable, goal, s, combi, elem)


i = 0
for c in combinations([1,2,5,10,20,50,100,200], 200):
    i += 1

print(i)

