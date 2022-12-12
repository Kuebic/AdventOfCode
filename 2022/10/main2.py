with open("input.txt") as file:
  INSTRUCTIONS = [line.split() for line in file]

INTERESTED = []
CRT = ""

def print_limit(arr, x):
    for i in range(int(len(arr)/x)):
        print(arr[i*x:i*x+x])

def close_enough(cycle, sprite):
    sprite_range = [sprite-1, sprite, sprite+1]
    print(sprite_range, cycle)
    return cycle%40 in sprite_range

def draw(cycle, sprite):
    global CRT
    if close_enough(cycle, sprite):
        CRT += '#'
    else:
        CRT += '.'

def execute(x, cycle, instruct):
    if instruct[0] == 'noop':
        draw(cycle, x)
        cycle += 1
        return (x, cycle)
    elif instruct[0] == 'addx':
        draw(cycle, x)
        cycle += 1
        draw(cycle, x)
        x, cycle = x+int(instruct[1]), cycle+1
        return (x, cycle)

def main():
    x = 1
    cycle = 1
    for instruct in INSTRUCTIONS:
        x, cycle = execute(x, cycle, instruct)
            

main()
print_limit(CRT, 40)