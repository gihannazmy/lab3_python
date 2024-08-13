def read(filepath, option):
    try:
        with open(filepath, 'r') as file:
            if option == 'all':
                return file.read()
            elif isinstance(option, int):
                return file.read(option)
            elif option == 'line':
                return file.readline()
            elif option == 'lines':
                return file.readlines()
            else:
                return 'Invalid option'
    except FileNotFoundError:
        return 'File not found'
    except Exception as error:
        return f'There was an error: {error}'

def write(filepath, content):
    if isinstance(content, str):
        try:
            with open(filepath, 'w') as file:
                file.write(content)
                return 'File written successfully'
        except Exception as error:
            return f'There was an error: {error}'
    else:
        return 'Invalid content, must contain a string'

def append(filepath, newcontent):
    try:
        with open(filepath, 'a') as file:
            if isinstance(newcontent, list):
                file.writelines(newcontent)
            else:
                file.write(newcontent)
        return 'Content appended successfully'
    except Exception as error:
        return f'There was an error: {error}'


print(read('asd.txt', 'all'))
print(write('asd.txt', 'This is a content.'))
print(append('asd.txt', '\nThis is an appended content.'))