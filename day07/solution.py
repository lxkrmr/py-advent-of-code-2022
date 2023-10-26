from day07.models import FlatFileSystem
from lib.utils import file_to_lines


class CommandLineParser:
    CHANGE_DIRECTORY = '$ cd '
    UP_ONE_DIRECTORY = '$ cd ..'
    LIST_DIRECTORY = 'dir '
    LIST_FILE_SEPARATOR = ' '

    def __init__(self):
        self.filesystem = FlatFileSystem.create_empty()

    def parse(self, lines: list[str]) -> None:
        for line in lines:
            self._parse(line)

    def _parse(self, line: str):
        if line == CommandLineParser.UP_ONE_DIRECTORY:
            self._up_one_directory()
        elif line.startswith(CommandLineParser.CHANGE_DIRECTORY):
            self._change_directory(line)
        elif line.startswith(CommandLineParser.LIST_DIRECTORY):
            self._list_directory(line)
        elif self._is_file_listing(line):
            self._list_file(line)

    def _up_one_directory(self):
        self.filesystem.up_one_directory()

    def _change_directory(self, line: str) -> None:
        _, directory_name = line.split(CommandLineParser.CHANGE_DIRECTORY)
        self.filesystem.change_directory(directory_name)

    def _list_directory(self, line: str) -> None:
        _, directory_name = line.split(CommandLineParser.LIST_DIRECTORY)
        self.filesystem.make_directory_if_not_exist(directory_name)

    @staticmethod
    def _is_file_listing(line: str) -> bool:
        return line[0].isdigit()

    def _list_file(self, line: str) -> None:
        file_size, file_name = line.split(CommandLineParser.LIST_FILE_SEPARATOR)
        self.filesystem.create_file_if_not_exist(file_name, int(file_size))


def part_one(lines: list[str]) -> int:
    command_line_parser = CommandLineParser()
    command_line_parser.parse(lines)
    return sum(
        [
            directory.size()
            for directory
            in command_line_parser.filesystem.list_directories()
            if directory.size() < 100_000
        ]
    )


def part_two(lines: list[str]) -> int:
    command_line_parser = CommandLineParser()
    command_line_parser.parse(lines)

    total_disk_space = 70_000_000
    used_space = command_line_parser.filesystem.root().size()
    total_space_needed_for_update = 30_000_000
    unused_space = total_disk_space - used_space
    additional_space_needed_for_update = total_space_needed_for_update - unused_space

    return min(
        [
            directory.size()
            for directory
            in command_line_parser.filesystem.list_directories()
            if directory.size() >= additional_space_needed_for_update
        ]
    )


def main():
    assert part_one(file_to_lines('test_input.txt')) == 95437
    print(part_one(file_to_lines('puzzle_input.txt')))

    assert part_two(file_to_lines('test_input.txt')) == 24933642
    print(part_two(file_to_lines('puzzle_input.txt')))

if __name__ == '__main__':
    main()
