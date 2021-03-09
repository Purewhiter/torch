'''
Author      : PureWhite
Date        : 2021-01-31 19:20:08
LastEditors : PureWhite
LastEditTime: 2021-02-04 21:20:32
Description : 
'''
def createCounter():
    def counter():
        n=1
        while True:
            yield n
            n+=1
        return n
    return counter


