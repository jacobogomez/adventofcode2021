def load_file(filename: str) -> list:
    with open(filename) as file:
        lines = file.readlines()

    return lines
