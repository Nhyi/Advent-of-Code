running_sum = 0

number_list = [
    ('one', 'on1e'),
    ('two', 'tw2o'),
    ('three', 'thr3e'),
    ('four', 'fou4r'),
    ('five', 'fiv5e'),
    ('six', 'si6x'),
    ('seven', 'seve7n'),
    ('eight', 'eigh8t'),
    ('nine', 'nin9e'),
]

with open(r'D:\Documents\Programming\Python Projects\Advent of Code\2023\Day 1\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line in text file.
    for line in lines:

        replacement = line

        for tp in number_list:
            if tp[0] in replacement:
                replacement = replacement.replace(tp[0], tp[1])

        values = [c for c in replacement if c.isdecimal()]
        running_sum += int(f'{values[0]}{values[-1]}')

    print(running_sum)