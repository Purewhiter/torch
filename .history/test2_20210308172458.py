'''
Author      : PureWhite
Date        : 2021-01-31 19:20:08
LastEditors : PureWhite
LastEditTime: 2021-03-08 17:24:58
Description : 
'''
from dearpygui import core, simple

def save_callback(sender, data):
    print("Save Clicked")

with simple.window("Example Window"):
    core.add_text("love")
    core.add_button("Save", callback=save_callback)
    core.add_input_text("string")
    core.add_slider_float("float")

core.start_dearpygui()