# Open the input file and read the contents
with open("input.txt") as file:
    contents = file.readlines()

# Initialize a variable to store the sum of priorities
priority_sum = 0

def commonletter(string):
    string1 = string[:len(string)//2]
    string2 = string[len(string)//2:]
    common = ""
    for char in string1:
        if char in string2:
            common = char
            break
    return common

def priority(letter):
    if not letter:
        # return 0
        raise ValueError("Input must be a non-empty string")
    score = ord(letter) - ord('a') + 1
    # print(letter.isupper())
    if letter.isupper():
        score += 26 + 32
    return score

# Loop over each rucksack
for rucksack in contents:
    common_item = commonletter(rucksack)
    # print(common_item)
    score = priority(common_item)
    # print(score)
    priority_sum += score
    # print("current total: " + str(priority_sum))

# Print the sum of priorities
print("final score is: " + str(priority_sum))
