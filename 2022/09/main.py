PATH = [x.split() for x in open("input.txt").readlines()]

'''
test.txt path = [['R', '4'], ['U', '4'], ['L', '3'], ['D', '1'], ['R', '4'], ['D', '1'], ['L', '5'], ['R', '2']]
answer should be: 13
'''

VISITED_LOC = set()

def move(t, diff):
  xdir = -1 if diff[0] < 0 else 1
  ydir = -1 if diff[1] < 0 else 1
  if abs(diff[0]) > 1 and diff[1] == 0:
    return [t[0] + xdir, t[1]]
  elif diff[0] == 0 and abs(diff[1]) > 1:
    return [t[0], t[1] + ydir]
  elif abs(diff[0]) > 1 or abs(diff[1]) > 1:
    return [t[0] + xdir, t[1] + ydir]
  else:
    return t

def compare(h, t):
  x = h[0] - t[0]
  y = h[1] - t[1]
  return x, y

def main():
  # convert array to bunch of string. ex: ['R', '4'] = RRRR
  fullpath = ''.join([c[0] * int(c[1]) for c in PATH])
  h = [0,0]
  t = [0,0]
  for i in fullpath:
    if i == 'R':
      h[0] = h[0] + 1
    elif i == 'L':
      h[0] = h[0] - 1
    elif i == 'D':
      h[1] = h[1] - 1
    elif i == 'U':
      h[1] = h[1] + 1
    diff = compare(h, t)
    t = move(t, diff)
    # print(h, t, diff)
    VISITED_LOC.add(tuple(t))
    # print(VISITED_LOC)

main()
print(f'Solution: {len(VISITED_LOC)}')
