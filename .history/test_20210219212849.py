'''
Author      : PureWhite
Date        : 2021-02-19 20:44:36
LastEditors : PureWhite
LastEditTime: 2021-02-19 21:28:49
Description : 
'''
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.setdefault('brand', 'white')
print(x)
