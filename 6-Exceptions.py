# # 6-2 Handling Exceptions
# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You have to input Numbers.")
#     print('ex: ', ex)
#     print('type(ex): ', type(ex))
# else:
#     print("No exceptions were thrown")


# 6-3 Handling Different Exceptions
# try:
#     age = int(input("Age: "))
#     xFactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You have to input correct numbers.")
# else:
#     print("No exceptions were thrown")


# # 6-4 Cleaning Up
# try:
#     file = open("6-Exceptions.py")
#     age = int(input("Age: "))
#     xFactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You have to input correct numbers.")
# else:
#     print("No exceptions were thrown")
# finally:
#     file.close()


# # 6-5 With Statement
# try:
#     with open("6-Exceptions.py") as file:
#         print("Open file here.")

#     age = int(input("Age: "))
#     xFactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You have to input correct numbers.")
# else:
#     print("No exceptions were thrown")


# 6-6 Raise Exception
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less...")
    return 10 / age


try:
    calculate_xfactor(0)
except ValueError as error:
    print('error: ', error)


# 6-7 Cost of Raising Exception
# "raise exception" consumes too much calicurate time.
# Only use it when you need it.
