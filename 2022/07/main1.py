stack = []
sizes = []

def up():
  sizes.append(stack.pop(-1))
  if stack:
    stack[-1] += sizes[-1]

for line in open("input.txt").readlines():
  match line.strip().split():
    case "$", "cd", "..": up()
    case "$", "cd", _: stack.append(0)
    case "$", _: pass
    case "dir", _: pass
    case size, _: stack[-1] += int(size)

while stack:
  up()

print(sum(s for s in sizes if s <= 100000))
print(min(s for s in sizes if s >= (max(sizes) - 40000000)))
