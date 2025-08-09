# numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 12, 3, 45, 6, 7, 890]
#                   ^
# iterate the numbers and print the first number that can be divided by 4

# for n in numbers:
#     if n % 4 == 0:
#         print(n)
#         break

# counter = 0
# for n in numbers:
#     if n % 4 == 0:
#         counter += 1
#         print(n)
#     if counter == 2:  # break condition
#         break
# print('hello')

# if the number contains 2 digits or more please dont print it
# otherwise print the number

# for n in numbers:
#     if n >= 10:
#         continue
#     print(n)

# ask the user to insert a password
# the user password is Gold123
# give the user 3 chances
# if the user hit the code stop asking him for password and greet him
# if the user starts the password with space ignore this try and ask him again

# password = 'Gold123'
# for i in range(1,4):  # [1,2,3]
#     guess = input('enter password : ')
#     if guess[0] == ' ':
#         continue
#     if guess == password:
#         print('welcome !!!!! ')
#         break
#     print(f'bad password maaaan tries : {3-i}')


# # shorthanded for
# salaries = [10000, 20000, 15000, 16000, 23456789]
#
# # those are the salaries for devshocko  we need to transfer the money to the account
# # wee need to calc the net salary by taking 47% AS a total taxes
#
# # net_salaries = []
# # for salary in salaries:
# #     net_salaries.append(salary * 0.53)
# #
# # print(net_salaries)
#
# list = [ what to append    for      if ]
# net_salaries = [x * 0.53 for x in salaries]
#
# print(net_salaries)
# # give me a list of the salaries that are greater than 15000
# height_salaries = [x for x in salaries if x > 15000]
# for x in salaries:
#     if x > 15000:
#         height_salaries.append(x)

# while

# x = 10
# while x < 100:
#     x += 1
#     print(x)
# print('hello')


# guess = ''
#
# while guess != 'Gold123':
#     guess = input('enter your password: ')

# ask the user to guess a number
# the number is random beteween 0-101

# import random
#
# print('Welcome to our hangman game !!!!!!!!!')
# start = int(input('enter the  start :'))
# end = int(input('enter the end :'))
#
# rnd = random.randint(start, end)
# guess = None
# tries = 0
#
# while rnd != guess:
#     guess = int(input(f'enter your guess (its a number {start}-{end})'))
#     if guess < 0:
#         print('you dont deserve to play')
#         break
#     if guess > end:
#         continue
#     tries += 1
#     if guess > rnd:
#         print('go lower V ')
#     else:
#         print('go greater ^')
# else:
#     print(f'took you {tries} time to guess the number')

# ask the user to insert ip's as a string
# validate that each ip have 3 point and save the ips to a list
# if the ip have a subnetmask  /X  please ignore it
# if the ip is longer than 20 chars break the loop
# if you have a 3 valid ips then exit the while loop
# hint len()

# ips = []
#
# while len(ips) < 3:
#     ip = input('enter ip : xxx.xxx.xxx.xxx ')
#     if '/' in ip:
#         print('skipping this try !!!!!!')
#         continue
#     if len(ip) > 20:
#         print('not a valid ip adios')
#         break
#     if ip.count('.') == 3:
#         ips.append(ip)
# else:
#     print(f'the valid ips : {ips}')

# list_em= [0:'hodi',1:1000]
employee = {'name': 'hodi', 'salary': 10000, 'car': 'mazda'}
#              key    value        pair
# print(employee)  # {'name': 'hodi', 'salary': 10000, 'car': 'mazda'}
# print(type(employee))  # <class 'dict'>
# print(employee['name'])  # hodi
# print(employee.get('car'))  # [] without errors
# print(employee.values())
# print(employee.keys())
# employee['fav_food'] = 'pizza'
# employee['name'] = 'yuval'
#
# print(employee)

# [(1, 1), (1, 1)]
for k, v in employee.items():
    if k == 'name':
        print(v.upper())