'''
Author      : PureWhite
Date        : 2021-02-19 20:44:36
LastEditors : PureWhite
LastEditTime: 2021-02-19 21:05:40
Description : 
'''

class Parrot:

# class attribute
 species = '鸟'

# instance attribute
 def __init__(self, name, age):
    self.name = name
    self.age = age

# instantiate the Parrot class
blu = Parrot('Blu', 10)
woo = Parrot('woo', 15)

# access the class attributes
print('Blu is a {}'.format(blu.__class__.species))
print('Woo is also a {}'.format(woo.__class__.species))
# access the instance attributes
print('{} is {} years old'.format( blu.name, blu.age))
print('{} is {} years old'.format( woo.name, woo.age))
