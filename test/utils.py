def load_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    return lines
