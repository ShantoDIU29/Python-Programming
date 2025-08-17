#some example if ,elif,else,and nested if elif statements
# Example: Check if a number is positive
num = 5

if num > 0:
    print("The number is positive.")

# Example: Check if a number is positive
num = 5

if num > 0:
    print("The number is positive.")
 
 # Example: Check if a number is positive, negative, or zero
num = 5

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Example: Check if a number is positive, negative, or zero, with nested if-elif statements
num = 5

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
