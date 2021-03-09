'''
Author      : PureWhite
Date        : 2021-02-19 20:44:36
LastEditors : PureWhite
LastEditTime: 2021-02-19 20:59:41
Description : 
'''

class Parrot:

 def fly(self):
   print('Parrot can fly')

 def swim(self):
   print('Parrot can not swim')

class Penguin:

 def fly(self):
   print('Penguin can not fly')

 def swim(self):
   print('Penguin can swim')

# common interface
def flying_test(bird):
  bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
