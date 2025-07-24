# # print("hello \nworld !")
# print('joey doesn\'t share food')  # this is a single line print
# print("1+2")
# print('''hello my name is hodi
# i love coffee
# and i love to eat pizza''')

# numbers in python
# print("1+5")  # output 1+5
# print(1+5)  # output 6

# operators
# print(1 + 10)  #
# print(1 - 10)  #
# print(4 * 40)  #
# print(2 ** 6)  # power
# print(10 / 3)  # divide 3.3333333
# print(10 // 3)  # divide 3
# print(10 % 3)  # modulo  1 <-> 10 - (3*(10//3))) =1

# 7 % 1 = 0
# 7 % 2 = 1
# 7 % 3 = 1
# 7 % 4 = 3
# 7 % 5 = 2

# 1 % 7 = 1
# 2 % 7 = 2
# 3 % 7 = 3
# 4 % 7 = 4
# 5 % 7 = 5
# 6 % 7 = 6
# 7 % 7 = 0

# even  vs  odd
# even : 2 , 4, 6
# odd : 1,3,5,189

# Datatypes

# print("1+1")  # string -> str
# print(1+1)  # number

## str operators

# + concat
# print('1' + "1")  # 11
# print('hothaifa' + ' ' + 'DevOps')
# print('htohaifaz'+'@hodicompany.com')  # concat
#
# print('-' * 50)

# print(True)  # bool
# print(type(True))
# print('*'*10)
# print(3.3)  # float
# print(type(3.3))
# print('*'*10)
# print(5)  # int
# print(type(5))
# print('*'*10)
# print('yaba daba dooo')  # str
# print(type('yaba daba dooo'))
# print('*'*10)

# grade = 90
# name = 'hothaifa'
# # var_name = value(datatype)
# print(grade)
# print(type(grade))


# declare assign

# x = 1 # x -> 1

# x, y, z = 1, 5, 9
# # x = 1
# # y = 5
# # z = 9
#
# print(z)

# casting
# a = int(1)  # a will be 1  a=1
# b = int(3.9)  # b will be 3
# c = int('3')  # c = will be 3
#
# print(c)
# print(type(c))


# float casting
# t = float(3.3)  # will be 3.3
# r = float(5)  # will be 5.0
# e = float('66.1')  # will be 66.1
#
# print(e)


# casting str

# f = str('hodi')  # will be hodi
# g = str(1)  # will be '1'
# h = str(True)  # will be 'True'
#
# print(h)
# print(type(h))

# casting bool truthy falsy

#       True         False
# int    1,-2          0
# float  1.1 0.05     0.0
# str  'hif' 'False'  ''
#
# a = bool(1994) # True
# b = bool(0) # False
# s = bool('')
# print(s)


# a = None
# print(type(a))

#
# is_healthy = True  # int 1
# is_ready = False  # 0

# print(is_ready + is_healthy + is_healthy)
# print(is_ready and is_healthy)
# print('*' * 6 + ' and ' + '*' * 6)
# print(True and False)
# print(True and True)
# print(False and True)
# print(False and False)
# print('*' * 6 + ' or ' + '*' * 6)
# print(True or False)
# print(True or True)
# print(False or True)
# print(False or False)


# name = 'ross'
# sen = 'we were on a break'
# print(name, sen, 9 + 18, sep='|', end='CC hothaifa\n')
# print('hunter x hunter')

# print('please enter you birth year: ',end='')
birth_year = int(input('please enter you b year :'))  # user_input = 12 -> str
name = input('please enter you name : ')
print('hi', name, 'your age is :', 2025 - birth_year)


print(f'hi {name} your age is {2025-birth_year}')