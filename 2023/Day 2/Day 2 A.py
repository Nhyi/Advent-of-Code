limit_dict = {'red': 12, 'green': 13, 'blue': 14}
game_sum = 0

with open(r'D:\Documents\Programming\Python Projects\Advent of Code\2023\Day 2\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line in text file.
    for line in lines:

        line = line.strip('\n').replace(' ', '')
        split_lines = line.split(':')
        game_num = int(split_lines[0].strip('Game'))
        games = split_lines[1].split(';')

        for game in games:
            