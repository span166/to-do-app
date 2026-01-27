"""
1. Module --> is a python file which contains functions.

A module in Python is a file containing Python code, such as function definitions, classes, and variables, that can be
reused in other Python programs. It is essentially a code library for organizing related functionality into a single .py
file, making programs easier to manage, maintain, and scale.

#2.  Version Control --> is the practice of recording the changes you make to your code. The software through which
                        this is achieved is know as version control system.

                        e.g - Git, Mercurial, Perforce.

A system that tracks and manages changes to files, especially source code, allowing developers to collaborate, revert
to older versions, and see who changed what and when, preventing lost work and enabling efficient teamwork on software
projects
"""


# 1. Using modules to import the functions/codes from other files.

'''
   One way of importing module. No need to write module name in the code below when calling get_todo and write_todo
   functions from the module.
'''

import todo_module

'''
   Another way of importing module. module name needs to be written in the code below when calling get_todo and 
   write_todo functions from the module.
   
   e.g --> import time
           time.sleep()
'''

import time                                   # importing time module. These are called standard module.
print( time.strftime("%b %d,%Y %H:%M:%S") )   # using the function inside the time module.


while True:

    user_input = input("Please type add, show, edit, clear or exit followed by your action: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):  # startswith with to validate the command at the start of the input.

        todos = todo_module.get_todo()  # Using functions to read the file. default arg value is already passed in fun.

        todo = user_input[4:] + "\n"  # Using slicing method to extract the user input followed by command.
        todos.append(todo)

        todo_module.write_todo("tododata.txt", todos)

    elif user_input.startswith("show") or user_input.startswith("display"):

        todos = todo_module.get_todo()  # Using custom functions to read the file.

        for index, item in enumerate(todos):
            item = item.strip("\n")  # This is to strip the break line characters in the output.
            print(f"{index + 1}.{item.title()}")

    elif user_input.startswith("edit"):
        try:  # This will be used to catch an error.
            todo_edit = int(user_input[5:])
            todo_edit = todo_edit - 1

            todos = todo_module.get_todo()  # Using custom functions to read the file.

            print(f"\n You have requested to edit - {todos[todo_edit]}")
            todos[todo_edit] = input("\n Enter new todo: ") + '\n'

            todo_module.write_todo("tododata.txt", todos)

        except ValueError:  # This will be used to catch an error.
            print("You have entered an incorrect command!")
            continue  # breaks the loop and send the control to the start of code.

    elif user_input.startswith("clear"):
        try:
            index_del = int(user_input[6:])
            usr_del = index_del - 1

            todos = todo_module.get_todo()  # Using custom functions to read the file.

            todo_to_be_removed = todos[usr_del].strip('\n')
            todos.pop(usr_del)

            todo_module.write_todo("tododata.txt", todos)

            message = f"You have deleted {todo_to_be_removed} from the todo list"
            print(message)

        except IndexError:
            print("There is no item in the todo with the number you have entered.")

    elif user_input.startswith("exit"):
        break

    else:
        print("\nThe command entered was not correct!!\n")

print("\nThank you, please visit our program again.")
