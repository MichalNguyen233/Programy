# Program to check if a number is even or odd

# Function to check if the number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# User input
num = int(input("Enter a number: "))

# Check and output the result
result = check_even_odd(num)
print(f"The number {num} is {result}.")