# Open the input file and read the contents
with open("input.txt") as file:
    contents = file.read()

# Initialize a variable to store the sum of priorities
priority_sum = 0

count = 0

per_line = contents.split('\n')

data = []

for i in range(int(len(per_line)/3)):
    data.append([per_line[count], per_line[count+1], per_line[count+2]])
    count += 3

same_letters = []

for i in data:
    same_letter = ''
    for rugzac in i:
        for letter in rugzac:
            if letter in i[0] and letter in i[1] and letter in i[2]:
                same_letter += letter
    same_letters.append(same_letter[0])

my_sum = 0

def priority(letter):
    if not letter:
        # return 0
        raise ValueError("Input must be a non-empty string")
    score = ord(letter) - ord('a') + 1
    # print(letter.isupper())
    if letter.isupper():
        score += 26 + 32
    return score

for i in same_letters:
    my_sum += priority(i)

print(my_sum)
