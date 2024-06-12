num = 1234321
r = 0
temp = num
while temp > 0:
    r = r*10+(temp % 10)
    temp = temp//10
    if r == num:
        print("palindrome", r)
    else:
        print("not palindrome", r)
