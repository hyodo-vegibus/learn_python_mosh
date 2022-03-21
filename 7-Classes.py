# # 7-3 Constructors
# class Point:
#     def __init__(self, x, y):  # magic method
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point {self.x}, {self.y}")


# point = Point(1, 2)
# print('point.x: ', point.x)
# point.draw()


# 7-4 Class vs Instance Attributes
# class Point:
#     default_color = "red"


# point = Point(1, 2)
# Point.default_color = "yellow"
# print('point.default_color: ', point.default_color)
# print('Point.default_color: ', Point.default_color)


# # 7-5 Class vs Instance Methods
# class Point:
#     def __init__(self, x, y):  # magic method
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point {self.x}, {self.y}")


# point = Point.zero()
# point.draw()


# # 7-6 Magic Methods
# class Point:
#     def __init__(self, x, y):  # magic method
#         self.x = x
#         self.y = y

#     def __str__(self):
#         # <- if there is no this magic method,
#         # you can not print out "point" itself.
#         return f"{self.x},{self.y}"

#     def draw(self):
#         print(f"Point {self.x}, {self.y}")


# point = Point(1, 2)
# print('point: ', point)


# 7-7 Comparing Objects
# 7-8 Performing Arithmetic Operations
# class Point:
#     def __init__(self, x, y):  # magic method
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         # if there is not this method,
#         # you will return false from print(point == other) down below.
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         # if there is not this method,
#         # you will return false from print(point > other) down below.
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(10, 22)
# other = Point(1, 2)
# print(point == other)
# print(point > other)

# combined = point + other
# print('combined.x: ', combined.x)
# print('combined.y: ', combined.y)


# 7-9 Making Custom Containers
# 7-10 Private Members (tags -> __tags)
# :it's not perfect secure, just for accidentally modifying
# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# cloud.add("Javascript")


# print("cloud.tags: ", cloud.__tags)
# print("cloud['python']: ", cloud["python"])

# cloud["python"] = 20
# print("cloud['python']: ", cloud["python"])

# print("len(cloud): ", len(cloud))

# for i in cloud.__tags:
#     print(i, cloud[i])


# 7-11 Properties
# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value


# banana = Product(50)
# print('banana.price: ', banana.price)

# del banana


# 7-12 Inheritance, -14 Method Overriding,


# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print('eat')


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         # <-- if there's no super(), this__init__ override Animal's __init__
#         self.weight = 200

#     def walk(self):
#         print('walk')


# class Fish(Animal):
#     def swim(self):
#         print('swim')


# blackbass = Mammal()
# blackbass.eat()
# print('blackbass.age: ', blackbass.age)
# print('blackbass.age: ', blackbass.weight)


# 7-15 Multi-level Inheritance
# !important! Avoid multi level inheritance not more than 4 level.


# 7-16 Multiple Inheritance
# When you use it,
# class Flyer:
#     def fly(self):  # <- don't have common methods or attributes
#         pass


# class Swimmer:
#     def swim(self):  # <- don't have common methods or attributes
#         pass


# class FlyerFish(Flyer, Swimmer):
#     pass


# 7-17 Good Example of Inheritance


# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

# # these classes below have only one level of inheritance
# # and not multiple inheritance


# class FileStream(Stream):
#     def read(self):
#         print('Reading data from a file')


# class NetworkStream(Stream):
#     def read(self):
#         print('Reading data from a network')


# class MemoryStream(Stream):
#     def read(self):
#         print('Reading data from a memory stream')


# stream = MemoryStream()
# stream.open()


# 7-19 Polymorphism
# I wan's sure what is important of this session.


# 7-21 Extending Built-in Types
# class Text(str):
#     def duplicate(self):
#         return self + self


# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)


# list = TrackableList()
# list.append(1)


# 7-22 Data Classes with namedtuple
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p1 = Point(x=10, y=2)
# <- Rewriting because namedtuple is immutable
# You cannot do like p1.x = 10
p2 = Point(x=1, y=2)
print(p1 == p2)
