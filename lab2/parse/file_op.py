def write_file(file_name, data: str):
    """ Функция записи данных в файл """
    try:
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
    except Exception as e:
        print(e)
    return 1


def read_file(file_name) -> str:
    """ Функция чтения данных(файла) """
    try:
        f = open(file_name, 'r')
        data = f.read()
        f.close()
    except Exception as e:
        print(e)
    return data