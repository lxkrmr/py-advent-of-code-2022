def file_to_str(filename: str) -> str:
    with open(filename, 'r') as file:
        result = file.read()
    return result


def file_to_lines(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        result = file.read().splitlines()
    return result
