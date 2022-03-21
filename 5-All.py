# 5-1
# letters = ["a", "b", "c"]
# zeros = [0] * 5
# print('zeros: ', zeros)

# combined = zeros + letters
# print('combined: ', combined)

# numbers = list(range(20))
# print('numbers: ', numbers)

# chars = list('Hello World')
# print('chars: ', chars)

# chars_length = len(chars)
# print('chars_length: ', chars_length)

# 5-2
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", ]
# print('letters: ', letters)
# print(letters[::])
# print(letters[2::])
# print(letters[:2:])
# print(letters[::3])

# 5-3
# numbers = list(range(6))
# print('numbers: ', numbers)
# first, *others, last = numbers

# print('first: ', first)
# print('others: ', others)
# print('last: ', last)

# 5-4
# letters = ["a", "b", "c", "d", "e", ]
# # enumerate makes a list of Tuple, Unpacking from Tuple
# for index, letter in enumerate(letters):
#     print(index, letter)

# 5-5
# letters = ["a", "b", "c", "d", "e", ]

# ADD
# letters.append('f')
# letters.insert(2, '-')

# REMOVE
# letters.pop()
# letters.remove('b')
# del letters[0:3]
# letters.clear()
# print('letters: ', letters)


# 5-6
# letters = ["a", "b", "c", "d", "e", ]

# if "d" in letters:
#     print(letters.index("d"))

# print('letters.count("a"): ', letters.count("a"))


# # 5-7
# numbers = [3, 51, 5, 4, 89, 434]
# numbers.sort()
# sortedNum = sorted(numbers, reverse=True)

# print('sortedNum: ', sortedNum)
# print('numbers: ', numbers)


# 5-8 Lambda
# from collections import deque
# products = [
#     ("product1", 2),
#     ("product1", 60),
#     ("product1", 42),
#     ("product1", 11),
# ]


# def sort_item(item):

#     return item[1]


# # products.sort(key=sort_item)

# # "iterable".sort(key=lambda parameter:expression)
# products.sort(key=lambda item: item[1])
# print('products: ', products)


# 5-9 Map
# map(lambda parameter: expression, "iterables")
# prices = list(map(lambda product: product[1], products))
# print('prices: ', prices)


# 5-10 Filter
# gt10 = list(filter(lambda product: product[1] >= 10, products))
# print('gt10: ', gt10)


# 5-11 Comprehension
# prices = [item[1] for item in products]
# print('prices: ', prices)

# gt10 = [item for item in products if item[1] >= 10]
# print('gt10: ', gt10)


# 5-12 Zip
# list1 = [1, 45, 23]
# list2 = [9, 12, 34]

# print(list(zip(list2, list1, "abd")))


# 5-13 Stacks - LIFO
# browsing_session = []
# browsing_session.append(1)
# browsing_session.pop()
# if not browsing_session:
#     browsing_session[-1]


# 5-14 Queues - FIFO
# queue = deque([])
# queue.append(1)
# queue.append(2)
# if queue:
#     queue.popleft()
# if not queue:
#     print('empty')
# print('queue: ', queue)


# 5-15 Tuple
# point = (1, 2)
# point = 1, 2, 3
# point = 1,
# point = (1, 2) + (3, 4)
# point = (1, 2) * 3
# point = tuple([1, 2])
# point = tuple('Hello World')

# print('point: ', point)
# print('point[1]: ', point[1])
# print('point[0:3]: ', point[0:3])
# print('type(point): ', type(point))


# 5-16 Swapping
# x = 10
# y = 11

# x, y = y, x

# print('x: ', x)
# print('y: ', y)


# 5-18 Set
# : Set is unoderded unique items, immutable, not have duplicate,
# you can not access with index like [0] or [1]
# numbers = [1, 1, 2, 3, 5]
# first = set(numbers)
# second = {1, 6}

# print('first: ', first)
# print('second: ', second)

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print('Yes')


# 5-19 Dictionary
# point = {"x": 1, "y": 2, }
# point = dict(x=1, y=3)

# point["x"] = 10
# point["z"] = 20

# if "a" in point:
#     print(point["a"])

# print(point.get("a", 0))

# del point["x"]

# print('point: ', point)

# for key in point:
#     print(key, point[key])

# # unpack with Tuple : dic.items()
# for tup in point.items():
#     print(tup)

# for key, value in point.items():
#     print(key, value)


# 5-20 Dictionary Comprehensions
# Comprehension for List
# from sys import getsizeof
# values = [x * 2 for x in range(5)]

# # Comprehension for Set
# values = {x * 2 for x in range(5)}

# # Comprehension for Dict
# values = {x: x * 2 for x in range(5)}

# values = (x * 2 for x in range(5))
# print('values: ', values)


# 5-21 Generator
# values = (x * 2 for x in range(100000))
# print('gen_size: ', getsizeof(values))

# values = [x * 2 for x in range(100000)]
# print('list_size: ', getsizeof(values))


# 5-22 Unpacking Operator
# first = [1, 2, 3, 5]
# second = [6, 7, 8]

# values = [*first, *second]
# print('values: ', values)


# firstDict = dict(x=10)
# secondDict = dict(x=1, y=99)
# combined = {**firstDict, **secondDict}
# print('combined: ', combined)


# Exercise
sentence = "This is a common interview question"

# My answer
# 1. split all letters
# letters = [*sentence]
# # print('letters: ', letters)

# # 2. Extract unique letters
# unique_letters = {*sentence}
# # print('unique_letters: ', unique_letters)

# # 3. Count how many unique letters exist in the sentence


# def countFunc(i):
#     count = 0
#     for j in letters:
#         if i == j:
#             count += 1
#     return count


# count = {i: countFunc(i) for i in unique_letters}
# print('count: ', count)


# # 4. Pick up the highest count and show its letter
# highest_count_letters = [
#     key for key, value in count.items()
#     if value == max(count.values())
# ]
# print('highest_count_letters: ', highest_count_letters)


# 1. Count character frequency and put it in Dictionary
# {"T" : 5, ...}

# Mosh's answer
# character_frequency = {}

# for char in sentence:
#     if char in character_frequency:  # <- point : Loop over "Keys"
#         character_frequency[char] += 1
#     else:  # <- point
#         character_frequency[char] = 1

# character_frequency_sorted = sorted(  # <- point
#     character_frequency.items(),
# # <- point : Unpack Dict to access to the Value of it
#     key=lambda kv: kv[1],  # <- point
#     reverse=True
# )

# print('character_frequency: ', character_frequency)
# print('character_frequency_sorted: ', character_frequency_sorted)


# print('character_frequency_sorted: ', character_frequency_sorted)
