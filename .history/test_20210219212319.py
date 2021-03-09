'''
Author      : PureWhite
Date        : 2021-02-19 20:44:36
LastEditors : PureWhite
LastEditTime: 2021-02-19 21:23:19
Description : 
'''

class Parrot:

# instance attributes
 def __init__(self, name, age):
   self.name = name
   self.age = age

# instance method
 def sing(self, song):
   return '{} sings {}'.format(self.name, song)

 def dance(self):
   return '{} is now dancing'.format(self.name)

# instantiate the object
blu = Parrot('Blu', 10)
# call our instance methods
print(blu.sing('Happy'))
print(blu.dance())
