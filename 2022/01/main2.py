# Read the input from the file
with open("input.txt") as f:
    lines = f.readlines()

# Initialize a list of tuples that will store the calories and the Elf number
calories = []

# Initialize the Elf number to 0
elf_number = 0

# Initialize the current calories to 0
current_calories = 0

# Loop through each line in the input
for line in lines:
    # If the line is blank, then we have reached the end of an Elf's inventory
    if line.strip() == "":
        # Add the current calories and Elf number to the list of calories
        calories.append((current_calories, elf_number))

        # Increment the Elf number
        elf_number += 1

        # Reset the current calories to 0
        current_calories = 0
    else:
        # Otherwise, add the calories from the current food item to the current calories
        current_calories += int(line)

# At the end, add the current calories and Elf number to the list of calories
calories.append((current_calories, elf_number))

# Sort the list of calories in descending order
calories.sort(reverse=True)

# Initialize the total calories to 0
total_calories = 0

# Loop through the top three Elves
for i in range(3):
    # Add the calories carried by the current Elf to the total calories
    total_calories += calories[i][0]

# Print the total calories carried by the top three Elves
print(total_calories)
