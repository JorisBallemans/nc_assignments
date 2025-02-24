#!/bin/bash

# Define the training and test files
TRAIN_FILE="english.train"
ENGLISH_TEST="english.test"
TAGALOG_TEST="lang/xhosa.txt"

# Loop through r values from 1 to 9
for r in {2..5}; do
    # Execute the command for english.test and save the output
    english_output=$(java -jar negsel2.jar -self "$TRAIN_FILE" -n 10 -r "$r" -c -l < "$ENGLISH_TEST")
    echo "$english_output" > "english_r${r}_output.txt"

    # Execute the command for tagalog.test and save the output
    # tagalog_output=$(java -jar negsel2.jar -self "$TRAIN_FILE" -n 10 -r "$r" -c -l < "$TAGALOG_TEST")
    # echo "$tagalog_output" > "xhosa_${r}_output.txt"
done

echo "All outputs have been saved in the respective files."