lines = open(r'Day 8\inputs.txt').read().split('\n')

forest = []
inner_forest = []

for i in range(len(lines)):

    if i == 0 or i == len(lines) - 1:
        forest.append(list(lines[i]))
    else:
        inner_forest.append(list(lines[i][1:-1]))
        forest.append(list(lines[i]))

outer_trees = 4 * (len(forest) - 1)

for i in range(1, len(inner_forest)-1):
    