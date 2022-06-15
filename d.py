#
# 2022.06.13.
#
# Created by 김성찬.
#

#
# 4 Comprehensions and Generators
#

title = '''Item 27: Use Comprehensions Instead of map and filter'''
print(title)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)

squares = [x**2 for x in a]
print(squares)

squares = map(lambda x: x**2, a)
print(list(squares))

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

even_squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(even_squares))