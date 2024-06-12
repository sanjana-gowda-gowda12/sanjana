s = input("enter the string:")
def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Given string is palindrome")
else:
    print("It is not palindrome")
