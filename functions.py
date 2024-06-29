FILEPATH = "todos.txt"
def get_todos(filename=FILEPATH):
    """ Read text file and return list from text file """
    with open(filename, 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write todos to text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)