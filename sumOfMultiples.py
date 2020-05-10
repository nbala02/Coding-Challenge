# Python 3.8.0
# The following code takes a number and returns the sum of all the multiples of 3 or 5


# Creating a function that takes a number and outputs the sum of all the multiples of 3 or 5
def sumOfMultiples(loop):
    # Variable to add the elements that return 0 when calculating the modulus
    total = 0

    # Use a for loop to iterate the amount of times as indicated by the user
    for i in loop:
        # For each iteration calculate the modulus of the current integer and 3 or 5
        # If the modulus of the current integer and 3 or 5 is equal to 0, then update the value of total by adding
        modulus3 = (i % 3 == 0)
        modulus5 = (i % 5 == 0)
        if modulus3 or modulus5:
            total += i
    # Return the total sum of all the multiples of 3 or 5
    print(total)


# Enter an integer
# Set the range of the for loop based on the user input
# Call the function sumOfMultiples
print("Enter a number: ")
userInput = int(input())
loop = range(userInput)
sumOfMultiples(loop)
