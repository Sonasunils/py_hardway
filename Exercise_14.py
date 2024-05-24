#Promting and passing

#It imports the argv variable from the sys module
from sys import argv

script, user_name = argv
prompt = '> '
# It prints a greeting message using the user's name and the script name.
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# It asks the user if they like the script and waits for their response.
likes = input(prompt)
# It asks the user where they live and waits for their response.
print(f"Where do you live {user_name}?")
lives = input(prompt)
# Asks the user what kind of computer they have and waits for their response.
print("What kind of computer do you have?")
computer = input(prompt)
# Finally, it prints out a summary including the user's responses to the questions.
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")