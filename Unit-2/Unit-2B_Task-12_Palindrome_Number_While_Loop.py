number = int(input("Enter an integer: "))
original = number
reverse = 0
temp = abs(number)
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
if number >= 0 and original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
