with open("input.txt") as file:
  instructions = [line.split() for line in file]

print(len(instructions))
interested = []

def is_interested(cycle):
    if ((cycle-20)%40) == 0:
        return True

def main():
    x = 1
    cycle = 1
    for instruct in instructions:
        if instruct[0] == 'noop':
            cycle += 1
            if is_interested(cycle):
                interested.append([cycle, x])

        if instruct[0] == 'addx':
            cycle += 1
            if is_interested(cycle):
                interested.append([cycle, x])
            cycle += 1
            x += int(instruct[1])
            if is_interested(cycle):
                interested.append([cycle, x])
    print(f'final x = {x} and final cycle = {cycle}')

main()
signal_strength_list = []
for i in interested:
    signal_strength = i[0] * i[1]
    signal_strength_list.append(signal_strength)
    print(f'cycle {i[0]} * x {i[1]} = {signal_strength}')
    
print(sum(signal_strength_list))