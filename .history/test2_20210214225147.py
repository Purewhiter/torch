'''
Author      : PureWhite
Date        : 2021-01-31 19:20:08
LastEditors : PureWhite
LastEditTime: 2021-02-14 22:51:46
Description : 
'''
import easyocr
reader=easyocr.Reader(['ch_sim','en'])
reader.readtext('1.jpg')


