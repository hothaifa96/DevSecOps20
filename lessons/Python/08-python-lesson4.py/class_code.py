# cpu_usage = abs(float(input("Enter CPU usage percentage: ")))
# # abs(n) -> positive n  -9  9    -119   119   6   6
# if cpu_usage >= 90:
#     print('critical !!!!!!! ')
# elif 70 <= cpu_usage < 90:
#     print('high :( ')
# elif 50 <= cpu_usage < 70:
#     print('medium :| ')
# elif cpu_usage < 50:  # else:
#     print('normal :) ')
# index    0             1        2   3
# gang = ['eliran', 'holtsa afora', 4, True]

# print(gang)
# print(len(gang))  # 4
# print(type(gang))  # <class 'list'>
# print(type(gang[0]))  # <class 'str'>
# print(gang[4]) # error
# print(gang[-3]) #holtsa afora
# print(gang[len(gang) // 2])

# word = gang[1]
# print(gang[1][0: len((gang[1])) // 2])

# print(gang[1][2]) # l   the third char in the second item

########### list methods #########
# employees = ['yuval', 'dani', 'neria', 'shlomi', 'mohammed']
#
# print(employees.count('yuval'))  # 1
# employees.append('or')
# print(employees)
# employees.remove() # value
# employees.pop() # index

# tuple
#
# t = tuple()
# t = ()
# print(t)

# t = (1, 55, 66, 77)
# print(t)
# print(type(t))
# print(t[2])
# t.append(22)

# t = ('hothaifa', 'zoubi')  # tuple
# t = list(t)  # list
# t.insert(1, 'sos')  # list
# t = tuple(t)  # tuple
# print(t)

# grades = [100, 200, 300, 300, 300, 300, 300]
# tuple_grades = (100, 200, 300, 300, 300, 300, 300)
# set_grades = {100, 200, 300, 300, 300, 300, 300}
#
# print(grades)
# print(tuple_grades)
# print(set_grades)
#
# set_grades.add(6600)
# print(set_grades)
# print(5500 in set_grades)

# loops
# DRY - Don't repeat yourself
# Range - 0-10

# print(range(1, 10))  # -> 123456789
# evens = list(range(0, 100, 2))  # 0,2,4,6,8,10,12...
# print(evens)
# print(list(range(0,-100,-3)))
# print(list(range(100,-1,-1))) #[100,99,]

# crate  a tuple with the numbers that can be
# divided by 7 within the range 0-77 including 77

# print(tuple(range(0, 78, 7)))  # 0 7 14 21 28 .... 77
#           V
# names = ['Donald', 'Yuval', 'yossil', 'montana']
# # lens = []
# # for name in names:
# #     lens.append(len(name))
# # print(lens)
#
# # print only the names that ends with l
# for name in names:
#     if name.endswith('l'):
#         print(name)

# for i in range(10):
#     print('hello')

# i) ask the user to insert 4 numbers
# print the max number of those 4
# numbers = []
# for i in range(4):
#     numbers.append(int(input('enter a number : ')))   #  [1,55,66,33]
# print(max(numbers))

# ii) write a python program to sum all the user inputs
# give the user tha option to insert 6 numbers

# sum = 0
# for i in range(6):
#     n = int(input(f'please enter the {i + 1} number: '))
#     sum += n  # sum = sum + n
#
# print(sum)

# multi = 1
# for i in range(6):
#     n = int(input(f'please enter the {i + 1} number: '))
#     multi *= n  # sum = sum * n
#
# print(multi)

# chars = ['a','b','a','a','c','w','t','t','t','t','t','t']
# codeshare.io/hodis

# define a new list that contains the unique values of chars
# hint: chars.count(char)
# unique_chars = list(set(chars))
# print(unique_chars)

points = [(1, 2), (1, 3), (2, 5), (2, 6), (1, 1), (3, 4), (4, 4)]
# points is a list of tuples
# sort and print this list to show the tuples
# in asc order by the second item in the tuple
# output =
# [ (1, 1),(1, 2), (1, 3), (3, 4), (4, 4) ,(2, 5), (2, 6) ]

# print(points)  # list[(),(),(),....]
# print(points[0])  # tuple (1,2)
# print(points[0][1])  # int  2
# print(points[1][1])  # int 3
# print(points[2][1])
# print(points[len(points) -1][1])
print(points)
for i in range(len(points)):
    # print(points[i][1])
    for j in range(0, len(points) - i - 1):
        if points[j][1] > points[j + 1][1]:
            points[j], points[j + 1] = points[j + 1], points[j]

print(points)