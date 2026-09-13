# getting the string from the user
def get_string():
    user_string = input("Please enter your word:")
    return user_string


# checking if the string is palindrome
def is_palindrome(user_string):
    return user_string == user_string[::-1]


# creating a main function to run the program
def main():
    answer = "y"
    while answer.lower() == "y":
        user_string = get_string()
        if is_palindrome(user_string):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

        print("End of program.")
        answer = input("Do you want to continue (y/n):")
    print("Have a great day!")


if __name__ == "__main__":
    main()
    