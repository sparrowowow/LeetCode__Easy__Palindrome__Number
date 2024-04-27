
# Given an integer x, return true if x is a palindrome, and false otherwise.

x = 123
y = 123321


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        print("This number is a palindrome!")
        return True
    else:
        print("This number isn't a palindrome!")
        return False

is_palindrome(x)
is_palindrome(y)