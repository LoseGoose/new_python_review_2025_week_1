# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")

# Get two numbers from the user and ask for their name to personalize the experience


name = input("What's your name? ")
# this input is always a string
print(f"Hi, {name}! Let's do some math.\n")
# is yout output
# ask for your birthday
# ask for yor favorite food
# ask for two numbers

# Create output sentences using f-strings
# using these 3 inputs

birthday = input("When's your birthday(MM/DD/YYYY)? \n")
food = input("What's your favorite food? \n")
num1 = int(input("Whats your 1st number? \n"))
num2 = int(input("Whats your 2nd number? \n"))
print(f"Your birthday is {birthday} and favorite food is {food} the numbers you chose are {num1} and {num2}.\n")
print(f"the sum of {num1} and {num2} is {num1 + num2}")




# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings