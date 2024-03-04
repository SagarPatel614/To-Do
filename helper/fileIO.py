FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write th eto-do items list in the text file.

    :param todos_arg: TO-DO list item to write to file
    :param filepath: Path to the local to-do file
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writeLines(todos_arg)
