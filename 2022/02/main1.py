# Read the input from the file
with open("input.txt") as f:
    lines = f.readlines()

# Initialize the total score to 0
total_score = 0

# Loop through each line in the input
for line in lines:
    # Split the line into the opponent's move and your move
    opponent_move, your_move = line.strip().split()

    # Initialize the score for the round to 0
    score = 0

    rock = 1
    paper = 2
    scissor = 3

    loss = 0
    draw = 3
    win = 6

    # rock
    if opponent_move == "A":
        if your_move == "X":
            score = rock + draw
        elif your_move == "Y":
            score = paper + win
        elif your_move == "Z":
            score = scissor + loss
    # paper
    elif opponent_move == "B":
        if your_move == "X":
            score = rock + loss
        elif your_move == "Y":
            score = paper + draw
        elif your_move == "Z":
            score = scissor + win
    # scissor
    elif opponent_move == "C":
        if your_move == "X":
            score = rock + win
        elif your_move == "Y":
            score = paper + loss
        elif your_move == "Z":
            score = scissor + draw

    # Add the score for the round to the total score
    total_score += score

# Print the total score
print(total_score)
