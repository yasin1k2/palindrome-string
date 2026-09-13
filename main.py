# imports and global valuable

# getting the string from the user
def get_string():
    user_string = input("Please enter your word::")
    return user_string


# checking if the string is palindrome
def check_string(user_string):
    if user_string == user_string[::-1]:
        return "The string is palindrome."
    else:
        return "The string is not a palindrome."


# creating a mani function to run the program
def main():
    user_string = get_string()
    print(check_string(user_string))
    print("End of program.")

# looping the program if needed
answer = "y"
while answer == "y" or answer == "Y":
    main()
    answer = input("Do you want to continue(y/n)::")
print("Have a great day!")