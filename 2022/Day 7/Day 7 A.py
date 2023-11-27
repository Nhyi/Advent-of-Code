from collections import defaultdict

system_dict = lambda: defaultdict(system_dict)
system = system_dict()

lines = open(r'Day 7\inputs.txt').read().split('\n')

level_dict = {}
level = 0

for line in lines:

    if '$' in line and line == '$ cd /':
        level = 0
        directory = '/'
        level_dict[level] = directory

        if directory not in system:
            system[directory] = None

    elif '$' in line and line == '$ cd ..':
        level -= 1
        directory = level_dict[level]

    elif '$' in line and line == '$ ls':
        directory = level_dict[level]

    elif '$' in line:
        level += 1
        dir = line.split(' ')[-1]

        if level in level_dict:
            level_dict[level].append(dir)
        else:
            level_dict[level] = [dir]

    if '$' not in line:

        try:
            file_size = int(line.split(' ')[0])
            file_name = line.split(' ')[1]

            print(file_size, file_name)

            system[directory][file_name] = file_size

        except ValueError:
            current_directory = line.split(' ')[1]

print(level_dict)
print(system)