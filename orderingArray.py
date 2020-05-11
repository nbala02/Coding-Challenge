# Python 3.8.0
# The following code takes in an array as an argument and shifts all of the zeros to the end of the array


# Create function that takes in an array as an argument and shifts all of the zeros to the end of the array
def orderingArray(numOfElements, arrayLength):
    # Create an empty array
    array = []

    # Use a for loop to add the values into the empty array
    for i in arrayLength:
        # Allow user to enter the elements based on the amount of elements the user indicated
        # Add each element into the empty array
        print("Enter the element: ")
        userInput = input()
        array.append(userInput)

    # Return the array with all the elements
    print(array)

    # Variable to track the elements that are not equal to zeros
    j = 0
    # Use a for loop to iterate based on the amount of elements the user indicated
    for i in arrayLength:
        # Statement to shift over the elements in the array if the elements is not equal to the string zeros
        if not array[i] == '0':
            # Update the value of j by adding the elements other than zero in each iteration
            array[j] = array[i]
            j += 1

    # Use while loop to shift all zeros to the end of the array
    # Update the value of j as we shift the values in the array
    # Return the updated array with all zeros shifted to the end
    while j < numOfElements:
        array[j] = 0
        j += 1
    print(array)


# Enter the number of elements
# Set arrayLength to the range of number of elements
# Call the function orderingArray
print("Enter the number of elements you would like to add into the array: ")
numOfElements = int(input())
arrayLength = range(numOfElements)
orderingArray(numOfElements, arrayLength)
