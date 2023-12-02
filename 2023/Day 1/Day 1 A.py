running_sum = 0

with open(r'D:\Documents\Programming\Python Projects\Advent of Code\2023\Day 1\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line in text file.
    for line in lines:
        values = [c for c in line if c.isdecimal()]
        running_sum += int(f'{values[0]}{values[-1]}')

    print(running_sum)