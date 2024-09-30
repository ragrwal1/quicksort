#!/bin/bash

# Compile the C++ quicksort code
g++ quicksort.cpp -o quicksortApp

# Prompt for the CSV input
if [ -t 0 ]; then
    echo "Enter a CSV of numbers (e.g., 3, 5, 1, 9):"
    read input
else
    read input
fi


# Remove all spaces from the input
clean_input=$(echo "$input" | tr -d ' ')

# Check if the input contains only numbers, commas, and no invalid characters
if [[ ! "$clean_input" =~ ^[0-9,]+$ ]]; then
    echo "Error: Input contains invalid characters. Only numbers, commas, and spaces are allowed."
    exit 1
fi

# Convert the CSV string into an array by splitting on commas
IFS=',' read -r -a number_array <<< "$clean_input"

# Check if the array is empty
if [ ${#number_array[@]} -eq 0 ]; then
    echo "Error: No numbers entered."
    exit 1
fi

# Run the C++ quicksort executable, passing the array elements as arguments
./quicksortApp "${number_array[@]}"
