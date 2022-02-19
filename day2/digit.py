#Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("type two digit number: ")

# get the first and second digit substracting then convert string to int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# add the two diigt number
result = int(first_digit) + int(second_digit)
print(result)