'''
Author      : PureWhite
Date        : 2021-02-19 20:44:36
LastEditors : PureWhite
LastEditTime: 2021-02-19 20:52:37
Description : 
'''

class Bird:

   def __init__(self):
     print('Bird is ready')

   def whoisThis(self):
     print('Bird')

   def swim(self):
     print('Swim faster')

# child class
class Penguin(Bird):

   def __init__(self):
     # call super() function
     super().__init__()
     print('Penguin is ready')

   def whoisThis(self):
     print('Penguin')

   def run(self):
     print('Run faster')

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
