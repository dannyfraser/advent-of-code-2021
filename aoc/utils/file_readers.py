def read_int_list(file_name):
    with open(file_name) as f:
        contents = f.readlines()
        return list(map(int, contents))

def read_generic_text(file_name):
    with open(file_name) as f:
        content = f.readlines()
        return content
        