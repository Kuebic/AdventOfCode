with open("input.txt") as file:
  trees = [line.rstrip() for line in file]

rows = []
for row in trees:
  rows.append(row)

def calc_score(tree, line):
  for i in range(len(line)):
    compare = line[i]
    if compare >= tree:
      return i + 1
  return len(line)

def scenicScore(tree, left, right, up, down):
  if left == []:
    return 0
  elif right == []:
    return 0
  elif up == []:
    return 0
  elif down == []:
    return 0
  left = list(reversed(left))
  up = list(reversed(up))
  s_left = calc_score(tree, left)
  s_right = calc_score(tree, right)
  s_up = calc_score(tree, up)
  s_down = calc_score(tree, down)
  return s_left * s_right * s_up * s_down

highest_score = 0
for row in range(len(rows)):
  print(rows[row])
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
    score = scenicScore(rows[row][tree], left, right, up, down)
    if score > highest_score:
      highest_score = score
    print("score: {} highest: {}".format(score, highest_score))

print(highest_score)
