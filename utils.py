def read_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def input_to(fun: callable, *args):
    fun(input(), *args)


def write(value: str):
    print(value, end="")
