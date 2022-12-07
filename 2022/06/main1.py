with open("input.txt") as file:
  signal = file.read()

def solve(marker):
  for i in range(marker, len(signal)):
    s = signal[i-marker:i]
    if len(set(s)) == marker:
      print(i)
      break

solve(4)
solve(14)
