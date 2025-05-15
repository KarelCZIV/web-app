FILEPATH = 'files/todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file adn return the list of to-do items """   # doc strings
    with open(filepath, 'r') as file_def:
        todos_def = file_def.readlines()
    return todos_def


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file_def:
        file_def.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())
