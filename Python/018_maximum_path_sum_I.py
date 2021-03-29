
for file in ['tree.txt', 'triangle.txt']:
    tree_lines = []
    with open(file, 'r') as tree_file:
        for line in tree_file.readlines():
            nums = [int(num) for num in line.split(' ')]
            tree_lines.append(nums)


    tree_sums = []
    for i, row in enumerate(tree_lines):
        if i == 0:
            tree_sums.append(row)
        else:
            new_sums = []
            prev_sums = tree_sums[i-1]
            for j, num in enumerate(row):
                if j == 0:
                    new_sums.append(prev_sums[0] + num)
                elif j == len(row) - 1:
                    new_sums.append(prev_sums[-1] + num)
                else:
                    sum = prev_sums[j] if prev_sums[j] > prev_sums[j-1] else prev_sums[j-1]
                    new_sums.append(sum + num)
            tree_sums.append(new_sums)

    print(file, ':', max(tree_sums[-1]))

