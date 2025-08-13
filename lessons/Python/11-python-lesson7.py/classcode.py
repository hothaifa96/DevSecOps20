import requests

#
# url = 'https://catfact.ninja/fact'
#
# response = requests.get(url)  # http req
#
# # print(f'response : {response.status_code}')  #
# # print(f'response.json() : {type(response.json())}')  # dict
# if 400 > response.status_code >= 200:
#     data = response.json()  # {fact: '...',length:'...'}
#     print(data['fact'])

# API
# the url returns a random fact each about cats each time
# fetch the data form this url
url = 'https://catfact.ninja/fact'

# i) print only the facts that contain the word cat
# ii) print 5 random facts about cats
# iii) ask the user how many facts they want's to get
# and print them their facts
# iv) ask the user for a specific word that he wants tha fact to
# contain , and keep searching a fact till he got it

# i
res = requests.get(url)  # fire the http request
if res.status_code // 100 in [2,3]:
    data = res.json()
    # print(data['fact'] if 'cat' in data['fact'] else 'naah')
    if 'cat' in data['fact']:
        print(data['fact'])
    else:
        print('where is my smelly cat ')

facts = []
for i in range(5):  # 0-4
    res = requests.get(url)  # fetching
    if res.status_code < 400:
        print('fetched successfully')
        data = res.json()
        # print(data['fact'])
        facts.append(data['fact'])
print(facts)


user_input = int(input('how many facts you need ?'))
for i in range(user_input):  # 0-4
    res = requests.get(url)  # fetching
    if res.status_code < 400:
        print('fetched successfully')
        data = res.json()
        print(data['fact'])


user_word = input('whats is the word that your looking for: ')

while True:
    res = requests.get(url)
    if res.status_code >= 400:
        url = input('change the url please ')
        continue
    data = res.json()
    if user_word in data['fact']:
        print(data['fact'])
        break
    print('not yet')
    
    
    
# functions 

import math
import time


def greet():
    print('hello')


def greet_with_name(name):
    print(f'hello {name}')


def greet_with_name_type(name: str):
    print(f'hello {name}')


def greet_with_name_default(name='hothaifa'):
    print(f'hello {name}')


def greet_two_emp(name1, name2):
    print(f'hello from yaba daba doooo {name1}')
    print(f'hello from yaba daba doooo {name2}')


def greet_class(students: list):
    for student in students:
        print(f'hello {student}')


def calc_average(a: float, b: float):
    my_avg = (a + b) / 2
    return my_avg


# greet()
# time.sleep(4)
# greet()
# m = max( [1, 23, 4, 5, 787] )
# print(m)

# greet_with_name('neomi')
# greet_with_name(123456789)
# name = input('give me your name : ')
# greet_with_name(name)

# greet_with_name_type('reut')
# greet_with_name_default() # hello hothaifa
# greet_with_name_default('mohammed')
# greet_two_emp('shlomi', 'yuval')
# class1 = ['minus', 'trump', 'elon', 'joe']
# greet_class(class1)
# greet_class(['a', 'b'])


# result = greet_class(['mohammed', 'shlomi'])
# print(result)


# result = len('hothaifa')
# s = 'hodi'.upper()
# [].append()
# print(s)

# student_avg = calc_average(55, 87)
# print(student_avg)


############### function exercise ####################

# i) write a function that receives r and calc print the parameter of
# a circle
# def parameter(r: float = 1):
#     print(3.14 * 2 * r)


# ii) write a function that receives r and calc and return the area of
# circle
# def area(r: float = 1):
#     a = 3.14 * r ** 2
#     return a


# radius = float(input('enter the radius of the circle :'))
# parameter(radius)
# print(area(radius))

# parameter = 3.14 *2 *r
# area = 3.14 * r ** 2


# declare a python function to check if the ip falling in Cidrs
# that we received
# call example  :   check_ip('11.55.25.25',['11.55.25.0/8','1.5.25.11/24'])


###################################################################
def parameter1(a, c, d, b=11):
    p = a + b + c + d
    return p


parameter1(1, 2, 3)
parameter1(b=2, c=1, a=44, d=19)


def parameter(*args):
    print(args)
    print(type(args))
    p = 0
    for arg in args:
        if not isinstance(arg, int):
            continue
        p += arg
    print(p)


def project(*args, number_of_students: int = 3):
    print(args)
    print(number_of_students)
    print('registering : .....')
    c = 0
    for student in args:
        if not isinstance(student, str):
            continue
        if c == number_of_students:
            break
        print(f'{student}', end=' ')
        c += 1
    print()


def user_access(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print('admin' in kwargs.keys())


# rectangle
# rec_par = parameter1(5, 2, 5, 2)
# print(f'rectangle parameter {rec_par}')

# parameter()
# parameter(1, 12, 45, 78, 9)
# parameter(1)
# parameter('hello')

# project('hodi', 'reut', 'raed', 'haim', number_of_students=1)

# admin devops developer qa
user_access(admin='hodi', devops='niati', developer='itay', qa='hadar')


