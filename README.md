# Review of my first shell scripting program.
## ari.py

My first shell scripting program calculates the Automated Readability Index (ARI) of text files.

 # The basic idea to solve this problem is as follows:
    Read the file content.
    Find the number of characters, words, and sentences present in the file.
    Declare a function (calculate_ari) that passes these values as arguments. By using these values, calculate the ARI.
    Pass the ARI value to another function (determine_grade_level) to find the grade level.

## How I find solution :

## Read file content and find required values:

    Refer to Google and ChatGPT and found that content=$(cat "$file") can store the content of the file.
    Found character, word, and sentence counts by:

          chars=$(echo -n "$content" | wc -m)
          words=$(echo -n "$content" | wc -w)
          sentences=$(echo -n "$content" | grep -o '[.!?]' | wc -l)
    I sometimes get stuck because the reading content and find values are different in shell scripting

## Function:

    Refer to Google to learn how to write functions in shell scripting and found the solution.
    In the function call, use calculate_ari $chars $words $sentences to pass the three values as arguments.
    Inside the function, assign the value of the first argument to the local variable chars using local chars=$1. Similarly, assign values to other variables.
    Find the ARI value by substituting values into the equation.
    Declare another function determine_grade_level() to find the grade. Use if, elif statements to check each test case.

## Program accuracy:

    Test cases were checked using different files containing different character counts, sentences, and words.
    








