# def greet(first_name, last_name):
#     print(f"hello, {first_name} {last_name}")
#     print("hi")


# def get_greeting(name):
#     return f"Hi {name}"


# def increment(num, by):
#     return num + by


# 4-4. Keyword Argument
# print(increment(2, by=1))

# 4-5. optional parameter
# def increment(num, by=1):
#     return num + by


# print(increment(4))

# 4-6. xarg (Tuple)
def multiply(*num):
    total = 1
    for n in num:
        total *= n
    return total


print('multiply(2, 3, 4, 5): ', multiply(2, 3, 4, 5))

# 4-7. xxarg


def save_user(**user):
    print('user: ', user)
    print('user["name"]: ', user["name"])


# multiple keyword arguments
save_user(name='John', age=22, id=1)

# 4-9 Debugging
# def multiply(*num):
#     total = 1
#     for n in num:
#         total *= n
#     return total


# print("Start")
# print('multiply(2, 3, 4, 5): ', multiply(2, 3, 4, 5))


# 4-12 Exercise
# def Fizz_Buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return("Fizz Buzz")
#     if input % 3 == 0:
#         return("Fizz")
#     if input % 5 == 0:
#         return("Buzz")
#     return input


# print('Fizz_Buzz(15): ', Fizz_Buzz(15))
