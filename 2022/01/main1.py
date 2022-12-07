# Open the input file and read in the lines
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Parse the input and extract the calories for each food item
calories = []
current_elf = 1
for line in lines:
    # If the line is empty, this indicates that we are starting a new Elf's inventory
    if line.strip() == '':
        current_elf += 1
        continue

    # Extract the calories for the current food item and add it to the list
    calories.append((current_elf, int(line.strip())))

# Use a dictionary to store the total calories for each Elf
elf_calories = {}
for elf, cal in calories:
    if elf not in elf_calories:
        elf_calories[elf] = 0

    elf_calories[elf] += cal

# Find the Elf with the most calories
max_calories = 0
max_elf = 0
for elf, cal in elf_calories.items():
    if cal > max_calories:
        max_calories = cal
        max_elf = elf

# Print the result
print(f"Elf {max_elf} is carrying the most calories ({max_calories}).")
