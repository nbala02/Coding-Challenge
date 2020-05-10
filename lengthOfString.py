# Python 3.8.0
# The following code takes a string of words and returns the length of the shortest word(s)

# Import string library
import string


# Creating a function that reads a string of words and outputs the length of the shortest word(s)
def lengthOfString(userInput):
    # Statement to output Empty String if the input string is empty
    if (userInput == " ") or (userInput == ""):
        print("Empty String")

    # Code will execute when the string is not empty
    else:
        # Take the input and split the string where there is a space
        # Use the map function to obtain the length of each word in the string
        # Add the length of each word into a list
        # Return the lowest value in the list
        arrayInput = userInput.split(" ")
        length = map(len, arrayInput)
        findLength = list(length)
        print("Output Smallest Length: ")
        print(min(findLength))

# Enter a string of words
# Use string to remove all punctuations
# Call the function lengthOfString
print("Input a string of words: ")
removePunctuation = input().translate(str.maketrans('', '', string.punctuation))
userInput = removePunctuation
lengthOfString(userInput)
