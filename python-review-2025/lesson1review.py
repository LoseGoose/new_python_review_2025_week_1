    #Part one: For each line of code below, write what type of variable is being stored (string, integer, or float). Write your answer as a comment next to each line of code.

first_name = "Bro" # for example: this is a string
food = "pizza"
email = "Bro123@fake.com"
age = 25
quantity = 3
price = 10.99
gpa = 3.2
distance = 5.5

#Part 2 – Predict the Output

#Without running the code, predict what each line will print:
print(f"Hello {first_name}") # for example: Hello Bro
print(f"You like {food}") # for example: You like pizza
print(f"Your email is: {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")


# Part 3 – Fix the Errors

# The following code has two mistakes.
# Find and fix them so it runs correctly.

name = "Bro"
food = "pizza"
print(f"Hello {name}")
print(f"You like {food}")

# Missing quotes and wrong variable name
food = "pizza"
print(f"You like {food}")

# Wrong f-string format
age = 17
print(f"You are {age} years old")

# Mismatched parentheses
price = 12.99
print(f"The total price is ${price}")
      

# Variable name spelled incorrectly
name = "Bro"
print("Hello {name}")

# Using + instead of commas
name = "Bro"
print("Hello {name}")

# Mixing single and double quotes incorrectly
email = "Bro123@fake.com"
print(f"Your email is: {email}")

# Forgot to include the f before the string
age = 21
print(f"You are {age} years old")

# Trying to use a number as a variable
cool = "yes"
print(f"Am I cool? {cool}")
# rules for variables names state that they cannot start with a number 
# cannot use reserved words like class, def, return, etc
# cannor use special characters like !,@,#,$,% etc

# Missing curly braces
quantity = 3
print(f"You are buying {quantity} items")

# Using a reserved keyword
class2 = "ECS"
print(f"You are in {class2}")



# Part 4 – Create Your Own

# Write a short Python program that:
age = 15
rating = 9
school = "John Hancock College Preperatory High School"
print(f"I am {age} I got to {school} and i give it a {rating}/10.")
# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.
#  Example:
movie = "Inception"
rating = 9.5
year = 2010
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")
