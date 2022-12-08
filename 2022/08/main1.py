with open("input.txt") as file:
  trees = [line.rstrip() for line in file]

rows = []
for row in trees:
  rows.append(row)

def isVisible(tree, left, right, up, down):
  # if it's on the edge
  if left == []:
    return True
  elif right == []:
    return True
  elif up == []:
    return True
  elif down == []:
    return True
  # if every tree to the left/right/up/down is shorter
  elif tree > max(left):
    return True
  elif tree > max(right):
    return True
  elif tree > max(up):
    return True
  elif tree > max(down):
    return True
  else:
    return False

count = 0
for row in range(len(rows)):
  length_of_row = len(rows[row])
  for tree in range(length_of_row):
    left = []
    right = []
    up = []
    down = []
    left.append(rows[row][:tree])
    left = list(left[0])
    right.append(rows[row][tree+1:])
    right = list(right[0])
    for above in range(row):
      up.append(rows[above][tree])
    for below in range(len(rows)-1-row):
      down.append(rows[below+row+1][tree])
    # print("left: {0}, right: {1}, up: {2}, down: {3}".format(left, right, up, down))
    if isVisible(rows[row][tree], left, right, up, down):
      count += 1

print(count)
