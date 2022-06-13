def append_file(path, content):
    a = open(path, "a")
    a.write(content)
    a.close()

def read_file_content(path):
    a = open(path, "r")
    output = a.read()
    a.close()
    return output