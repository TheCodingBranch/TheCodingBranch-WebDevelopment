#!/usr/bin/env python3

# variable that is a STRING
example_variable = "Python is too easy 🎉"

# log what the VARIABLE is
print(example_variable)

# variable that is a boolean
true_or_false = True

# log true or false as a STRING
print("True or False: " + str(true_or_false))

# variable that is a FLOAT not an INT
number = 3.14

# log FLOAT and an int, cuts of decimal
print(f"The num is: {int(number)}")

# change variable into INT
number = 3

# log the INT
print(f"The num is: { number }")

num = 1

num = num + 5
print(f"The num currently is {num}")
num = num - 5
print(f"The num currently is {num}")
num = num * 5
print(f"The num currently is {num}")
num = num / 5
print(f"The num currently is {num}")

# variable that contains list
fruit_list = ["apple", "banana", "cherry"]
print(f"My list of fruit is {fruit_list}")



while num <= 10:
    print(f"The num is {int(num)}")
    num += 1

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(f"The number is {number}")

def find_my_favorite_fruit():
    for fruit in fruit_list:
        if fruit == "apple":
            return print(f"{fruit}'s are my favorite though!")

find_my_favorite_fruit()


def multiply_by_two(x):
    answer = x * 2
    return f"{x} multiplied by 2 is {answer}"

print(multiply_by_two(5))
