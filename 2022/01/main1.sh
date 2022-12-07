# Read in the input file and store it in a variable
input=$(cat input.txt)

# Parse the input and extract the calories for each food item
calories=()
current_elf=1
while read -r line; do
    # If the line is empty, this indicates that we are starting a new Elf's inventory
    if [[ -z "$line" ]]; then
        current_elf=$((current_elf+1))
        continue
    fi

    # Extract the calories for the current food item and add it to the array
    calories[$current_elf]=$((calories[$current_elf]+$line))
done <<< "$input"

# Find the Elf with the most calories
max_calories=0
max_elf=0
for elf in "${!calories[@]}"; do
    if [[ ${calories[$elf]} -gt $max_calories ]]; then
        max_calories=${calories[$elf]}
        max_elf=$elf
    fi
done

# Print the result
echo "Elf $max_elf is carrying the most calories ($max_calories)."
