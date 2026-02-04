'''

#1. pypi.org  --> Website to find, install and publish pyhton packages.

#2. You need to convert the .py file into an .exe (for Windows users), an .app file (for Mac users) or a .deb file
     (for Linux users) to use the python program as an desktop app.

#3. To make web apps, you need to use a Python web framework. The most popular web frameworks are Django, Flask, and
    Streamlit. In fact, Python is way better for building web apps.

'''

import todo_module
import FreeSimpleGUI as sg    # Importing the GUI package with an alias.
import todo_module
import time

# Below are the various instances created using the freesimplegui package.

clock_prompt = sg.Text('', key='clock')

label = sg.Text("Please enter a todo")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
button = sg.Button("Add")

list_box = sg.Listbox(values=todo_module.get_todo(), key='Itemlist',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
del_button = sg.Button("Clear")
exit_button = sg.Button("Exit")

sg.theme("Purple")                             # To set the theme of the GUI window.

window = sg.Window("My To-do App",
                   layout=[[clock_prompt],
                           [label, button],
                           [input_box],
                           [list_box, edit_button, del_button],
                           [exit_button]],
                   font=('Helvetica', 10))

while True:
    event, value = window.read(timeout=200)              # read() returns a tuple. Assigning values multiple variables.
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = todo_module.get_todo()
            new_todo = value['todo']
            todos.append(new_todo + '\n')

            todo_module.write_todo(todos)

            window['Itemlist'].update(values=todos)

        case 'Itemlist':                          # This is to send the real time update to label when item is selected.
            window['todo'].update(value=value['Itemlist'][0])

        case 'Edit':
            try:                                         # Try and except block to catch index error.
                todo_to_edit = value['Itemlist'][0]      # Storing the value of todo which user wants to edit.
                new_todo = value['todo']                 # Storing the new todo which user will edit to.
                todos = todo_module.get_todo()           # Reading the todo file.

                index = todos.index(todo_to_edit)        # finding out the index of the todo to edit.
                todos[index] = new_todo + '\n'           # Updating the todos locally created list.

                todo_module.write_todo(todos)            # Writing the edited todo to the file.

                window['Itemlist'].update(values=todos) # This is for real time update in the list when editing is done.

            except IndexError:                           # sg.popup is used to display a popup window.
                sg.popup("Please select a todo to edit", title='Error')

        case 'Clear':
            try:
                todo_to_clear = value['Itemlist'][0]
                todos = todo_module.get_todo()
                todos.remove(todo_to_clear)
                todo_module.write_todo(todos)

                window['Itemlist'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select a todo to delete", title='Error')

        case 'Exit':                                # Implementing the break for Exit button.
            break

        case sg.WIN_CLOSED:                         # This is to close the gui when the cross icon is clicked in GUI.
            break

window.close()



