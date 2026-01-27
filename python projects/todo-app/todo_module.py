# 1. This is a module which contains get_todo() and write_todo() functions.

def get_todo(filepath = "tododata.txt"):

    with open(filepath, 'r') as file_local:  # file_local is a local variable outside the main code.
        todos_local = file_local.readlines()  # todos_local is a local variable outside the main code.
    return todos_local                        # returns when called by the function.


def write_todo(filepath, todos_para):          # filepath and todos_para are parameter to the function.
    with open(filepath, 'w') as file_local:    # This function does not need return anything as it is doing something.
        file_local.writelines(todos_para)


# 2. Below lines in the code are used to test the module separately and when imported by function will not be executed.
"""
a. when imported the value of __name__ variable is the file name. {e.g --> __name__ = module_main5}.

b. Whereas when it is run within the module the value of __name__ variable is equal to __main__ which allows the if 
   block to be executed. 

"""
# print(get_todo())

if __name__ == "__main__" :
    print("This will be executed as a part of module only and not when imported by a main function.")