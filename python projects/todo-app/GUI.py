'''
#1. pypi.org  --> Website to find, install and publish pyhton packages.

'''

import todo_module
import FreeSimpleGUI as sg    # Importing the GUI package with an alias.

# Below are the various instances created using the freesimplegui package.

lable = sg.Text("Please enter a todo")
input_box = sg.InputText("")
button = sg.Button("Add")

window = sg.Window("My To-do App",layout = [[lable, button],[input_box]])
window.read()
window.close()



