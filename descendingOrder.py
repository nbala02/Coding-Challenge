# Python 3.8.0
# The following code takes non-negative integers and return it in descending order


# Creating a function that reads non-negative integers and outputs it in descending order
def descendingOrder(userInput):
    # Statement to make sure the input is a digit or a non-negative number
    if userInput.isdigit():

        # Add the input digits into a list
        # Sort the list from smallest to largest digits
        # Reverse the list to get the digits in descending order
        input_list = list(userInput)
        input_list.sort()
        input_list.reverse()

        # Join the digits together and print the list in descending order
        print("Output the descending list of numbers: ")
        print(''.join(input_list))

    # Output Invalid if the input is a negative integer
    else:
        print("Invalid Integer Input")


# Enter the list of numbers
# Call the function descendingOrder
print("Input a list of numbers: ")
userInput = input()
descendingOrder(userInput)
