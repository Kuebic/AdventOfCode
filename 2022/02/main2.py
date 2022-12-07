# Read the input from the file
with open("input.txt") as f:
    lines = f.readlines()

# Initialize the total score to 0
total_score = 0

# Loop through each line in the input
for line in lines:
    # Split the line into the opponent's move and the desired outcome
    opponent_move, outcome = line.strip().split()

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
        if outcome == "X":
            score = scissor + loss
        elif outcome == "Y":
            score = rock + draw
        elif outcome == "Z":
            score = paper + win
    # paper
    elif opponent_move == "B":
        if outcome == "X":
            score = rock + loss
        elif outcome == "Y":
            score = paper + draw
        elif outcome == "Z":
            score = scissor + win
    # scissor
    elif opponent_move == "C":
        if outcome == "X":
            score = paper + loss
        elif outcome == "Y":
            score = scissor + draw
        elif outcome == "Z":
            score = rock + win

    # Add the score for the round to the total score
    total_score += score

# Print the total score
print(total_score)
