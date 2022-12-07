import re

stacks = []

# with open("test.txt") as file:
#     data = file.read()
data = open("input.txt")

for line in data:
  if line == "\n": break
  stacks.append([line[k * 4 + 1] for k in range(len(line) // 4)])

stacks.pop()
stacks = [list("".join(c).strip()[::-1]) for c in zip(*stacks)]

for line in data:
  how_many, stack_from, stack_to = map(int, re.findall("\\d+", line))
  stacks[stack_to - 1].extend(stacks[stack_from - 1][-how_many:][::-1])
  stacks[stack_from - 1] = stacks[stack_from - 1][:-how_many]

print("".join([a[-1] for a in stacks]))
