# Review of my first shell scripting program.
## ari.py

My first shell scripting program is about to calculate Automated redability index of text files.


## The basic idea about to solve this problem :


1.Read the file content.


2.Find the number of characters,words and sentance present in the file.


3.Declar a function(calculate_ari) pass these value as argument.By using these value calculate ARI.


4.The ARI value passsed to an another function(determine_grade_level) for finding grade.

## How I find solution :


Read file content and find required values.


Refer google and chatgpt and find `**content=$(cat "$file")` can store content of file and i find character, words and sentance by `chars=$(echo -n "$content" | wc -m)`
`words=$(echo -n "$content" | wc -w)`
`sentences=$(echo -n "$content" | grep -o '[.!?]' | wc -l)`

Function

Refer google how to write function in shell scripting. And find the solution .In function call `calculate_ari $chars $words $sentences` Pass 3 values as argument. `local chars=$1 ` Assign value of the first argument to the local variable "chars".Like that all the argument values are assign to variables. And find ARI value by substituting values to Equation  .
Declear another function `determine_grade_level()` for finding grade.Using if elif each test cases were checked.

## Program accuracy

Test cases checked by using different files containing different character count , sentence and words..







