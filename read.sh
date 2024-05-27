#!/bin/bash

# Function to calculate ARI
calculate_ari() {
    local chars=$1
    local words=$2
    local sentences=$3

    local ari=$(echo "scale=2; 4.71 * ($chars / $words) + 0.5 * ($words / $sentences) - 21.43" | bc)
    echo "Automated Readability Index (ARI): $ari"
    determine_grade_level $ari
}

# Function to determine grade level based on ARI score
determine_grade_level() {
    local ari=$(echo "$1" | awk '{print int($1+0.5)}')

    if [ $ari -le 0 ]; then
        echo "Grade Level: Kindergarten (5-6 yrs old)"
    elif [ $ari -eq 1 ]; then
        echo "Grade Level: First Grade (6-7 yrs old)"
    elif [ $ari -eq 2 ]; then
        echo "Grade Level: Second Grade (7-8 yrs old)"
    elif [ $ari -eq 3 ]; then
        echo "Grade Level: Third Grade (8-9 yrs old)"
    elif [ $ari -eq 4 ]; then
        echo "Grade Level: Fourth Grade (9-10 yrs old)"
    elif [ $ari -eq 5 ]; then
        echo "Grade Level: Fifth Grade (10-11 yrs old)"
    elif [ $ari -eq 6 ]; then
        echo "Grade Level: Sixth Grade (11-12 yrs old)"
    elif [ $ari -eq 7 ]; then
        echo "Grade Level: Seventh Grade (12-13 yrs old)"
    elif [ $ari -eq 8 ]; then
        echo "Grade Level: Eighth Grade (13-14 yrs old)"
    elif [ $ari -eq 9 ]; then
        echo "Grade Level: Ninth Grade (14-15 yrs old)"
    elif [ $ari -eq 10 ]; then
        echo "Grade Level: Tenth Grade (15-16 yrs old)"
    elif [ $ari -eq 11 ]; then
        echo "Grade Level: Eleventh Grade (16-17 yrs old)"
    elif [ $ari -eq 12 ]; then
        echo "Grade Level: Twelfth Grade (17-18 yrs old)"
    else
        echo "Grade Level: College (18-22 yrs old)"
    fi
}

# Check if the file is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

file=$1

# Check if the file exists
if [ ! -f "$file" ]; then
    echo "File not found!"
    exit 1
fi

# Read the file content
content=$(cat "$file")

# Count characters, words, and sentences
chars=$(echo -n "$content" | wc -m)
words=$(echo -n "$content" | wc -w)
sentences=$(echo -n "$content" | grep -o '[.!?]' | wc -l)

# Ensure there's at least one sentence to avoid division by zero
if [ $sentences -eq 0 ]; then
    sentences=1
fi

# Output the counts (for debugging purposes)
echo "Characters: $chars"
echo "Words: $words"
echo "Sentences: $sentences"

# Calculate and display ARI
calculate_ari $chars $words $sentences
