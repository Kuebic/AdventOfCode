# Open the input file and read the contents
with open("./04/input.txt") as file:
    contents = file.readlines()

range_pairs = []

for line in contents:
    pair = line.replace('\n','').split(',')
    range_pairs.append(pair)

counter = 0

for pair in range_pairs:
    # split the rante into the start and end values
    range1 = pair[0].split('-')
    range2 = pair[1].split('-')
    # check if one range fully contains the other
    if (int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1])) or (int(range2[0]) <= int(range1[0]) and int(range2[1]) >= int(range1[1])):
        counter += 1

print(counter)
