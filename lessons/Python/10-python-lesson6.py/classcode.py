# import datetime
# import time
#
# while datetime.datetime.now().minute < 24:
#     print(datetime.datetime.now().second)
#     time.sleep(1)
# ask the user for username check if it starts with z
# if not ask him again for the username


# username = input('enter your username :')  # dry violation
# while not username.startswith('z'):
#     username = input('enter your username :')  # dry violation
#
# print('welcome')

# do while
# while True:
#     username = input('enter your username :')
#     if username.startswith('z'):
#         break
# print('welcome')


######## dict #########
#          0   1  2    3  4
# grades = [11, 19, 99, 68, 79]
#
# grades_dict = {'hodi': 11, 'raed': 19, 'shlomi': 99, 'max': 68, 'shay': 79}
#
# car = {'make': 'byd', 'model': 'atto3', 'distance': 404, 'ev': True, 'belts': [False, False, False, False, False]}

# read
# print(car)
# print(type(car))
# print(len(car))  # number of items
# # print(car['1']) #error
# # print(car[1]) #error
# print(car['make'])  # byd
# print(car['ev'])  # True
# # print(car['wheels']) # Error
# print(car.get('wheels'))  # None
# print(car)  # 404
# car['distance'] = 555
# car['color'] = 'grey'  # add new item
# print(car)  # 555
# print(car)
# car.clear()
# del car['make'] # delete item
# car.pop('distance')
# data = 'make'
# print(data in car.keys())
# print(car[data])
# print(car)
#
# print(car.keys())
# print(car.values())
# print(car.items())
# print(car)


# loops jsons
# pip
# imports
# rest api
# requests


# json

# declare a dict of students per class : A B C D E F
# { 'class_A' : 42 , }
# import random
# import math
# import time
# import datetime
# import os

#
# classes = {'class_A': random.randint(0, 50), 'class_B': random.randint(0, 50), 'class_C': random.randint(0, 50),
#            'class_D': random.randint(0, 50), 'class_E': random.randint(0, 50), 'class_F': random.randint(0, 50)}
# # i)   print the number of the students in the E class
# # ii)  print all the classes names
# # iii) override the class_A to 0 students and add new class named x with 20 students
# # iv)  calc the average students per class (loop?)
#
# # print(classes)
# #
# # print(f'the number of the students in E is : {classes["class_E"]}')
# # print(list(classes.keys())) #['class_A', 'class_B', 'class_C', 'class_D', 'class_E', 'class_F']
# # classes['class_A'] = 0  # override
# # classes['class_X'] = 20  # assign
# #
# # print(classes)

# sum = 0
# for value in classes.values():  # [22, 23, 42, 1, 11, 13]
#     sum += value
# # print(sum)
# classes_len = len(classes.values())
# avg = sum/classes_len
# print(math.ceil(avg))
#
# sum = sum(classes.values())
# print(sum/len(classes.values()))

#
# employee = {'name': ['haim', 'or'], 'car': "audi rs7", 'role': 'DevOps Eng', 'salary': 32000, 'office days': 3,
#             'cibus': 1140}
#
# # print the name of the employee
# # print(employee['name'])
# # check if the employee object contain a car key ?
# # if not employee.get('car'):
# #     print('the employee have no car ')
# #
# # if 'car' not in employee.keys():
# #     print('the employee have no car ')
#
# print(employee.items())  # [(),(),()]
# # for item in  employee.items():
# #     for i in item:  #(key,value)
# #         print(i)
# sim = 0
# for k, v in employee.items():
#     # k -> key , v -> value
#     print(f' the key is {k} and the value is {v}')
#     if k == 'salary' or k == 'cibus':
#         sim += v
#     if isinstance(v, list):  # check if the v is list
#         for s in v:
#             if s == 'haim':
#                 print('shakshoka')
#             else:
#                 print(s)
# print(sim)


######################   pip    ###################
#
# from PIL import Image
#
# choice = input('what image you want to see : (panda, pizza)')
# im = Image.open('panda.jpg') if choice == 'panda' else Image.open('download.jpg')
# im.resize((1300,1100))
# im.show()


######## requests #######
import requests

# url = 'https://jsonplaceholder.typicode.com/users'
# response = requests.get(url)
# print(response)
# print(response.status_code)
# if 200 <= response.status_code < 300:
#     print('success response')
#     print(type(response.json())) # list
#     print(type(response.json()[1])) # dict
#     data = response.json()
#     for user in data: # [{},{},{}]
#         print(f'this is : {user["name"]}  email: {user["email"]}')

# send http request to https://jsonplaceholder.typicode.com/users and
# print all the user's names

# send http requests to https://jsonplaceholder.typicode.com/posts
# and print all the titles of the posts that contains at least 60 chars
# print me the number of spaces in those title that are more than 60 chars

url = 'https://jsonplaceholder.typicode.com/posts'

res = requests.get(url)
if res.status_code == 200:
    print('fetched successfully')
    posts = res.json()
    print(len(posts))  # list
    for post in posts:
        # print(type(post)) # dict
        if len(post.get('title')) > 60:
            print(post['title'])
            print(f'spaces : {post["title"].count(" ")}\nwords: {post["title"].count(" ") +1} ')
