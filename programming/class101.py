

# Agorithms 101
# Input should be two digit numbers between 10-99
# User should not input any other data type
# Input should not be more than or less than two digit number


# Enter a value
enter_value = input("Enter a value pair between (10 - 99): ")
    # todo
    # test for test cases

if len(enter_value) > 2:
    print("Enter your value again")
    enter_value = input("Enter a value pair between (10 - 99): ")
elif len(enter_value) < 2:
    print("Enter your value again")
    enter_value = input("Enter a value pair between (10 - 99): ")
elif enter_value.isalpha():
    print("Enter a number")
    enter_value = input("Enter a value pair between (10 - 99): ")
elif len(enter_value) == 2:
    # Convert value to list
    saved_number = list(enter_value)
    # print(saved_number)
        # Extract value, convert to int and sum
    sum_saved_number = int(saved_number[0]) + int(saved_number[1])
        # print result
    print(sum_saved_number)

# assignment
# Display the error
# prompt the user to input again
# the sum of the number must not be bigger than 9.

# if sum_saved-number > 0 and sum_saved_number < 10:

# number = input("Ener number: ")

# while number.isalpha() or len(number) > 2 or len(number) < 2 or "." in number or number[0] = "-":
#     if number.isalpha():
#         number = input("Nmber is alpha")
#     elif "." in number:
#         number = input("number is a float")
#     elif len(number) > 2 or len(number) < 2:
#         number = input("length of number is less than 2")
#     elif number[0] == "-":
#         number = input("Number is negative")
#     sum_of_numbers = int(number[0]) + int(number[1])

#     while sum_of_numbers > 9:
#         number = input("sum is greater than 9")
#         print(sum_of_numbers)
