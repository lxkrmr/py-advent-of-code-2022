from dataclasses import dataclass
from typing import Optional


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    ROOT = '/'
    name: str
    parent: 'Directory'
    children: dict[str, 'Directory']
    files: dict[str, File]

    @classmethod
    def create_empty(cls, name: str, parent: 'Directory') -> 'Directory':
        new_dir = cls(name=name, parent=parent, children={}, files={})
        if parent:
            parent.add_child(new_dir)
        return new_dir

    def size(self) -> int:
        direct_file_sizes = [file.size for file in self.files.values()]
        indirect_file_sizes = [directory.size() for directory in self.children.values()]
        return sum(direct_file_sizes + indirect_file_sizes)

    def add_child(self, child: 'Directory') -> None:
        path = create_path(child.name, self)
        self.children[path] = child

    def add_file(self, file: File) -> None:
        self.files[file.name] = file


@dataclass
class FlatFileSystem:
    working_directory: Directory | None
    register: dict[str, Directory]

    @classmethod
    def create_empty(cls) -> 'FlatFileSystem':
        return cls(None, {})

    def change_directory(self, directory_name: str) -> None:
        directory = self._get_or_create(directory_name)
        self.working_directory = directory

    def make_directory_if_not_exist(self, directory_name) -> None:
        self._get_or_create(directory_name)

    def up_one_directory(self) -> None:
        if self.working_directory and self.working_directory.name == Directory.ROOT:
            print(f'Already in {Directory.ROOT}, will not change directory')
            return

        self.working_directory = self.working_directory.parent

    def list_directories(self) -> list[Directory]:
        return [*self.register.values()]

    def root(self):
        return self.register.get(Directory.ROOT)

    def _get_or_create(self, directory_name: str) -> Directory:
        directory = self._get_directory(directory_name)
        if directory is None:
            directory = self._make_directory(directory_name)

        return directory

    def _get_directory(self, directory_name: str) -> Directory:
        path = create_path(directory_name, self.working_directory)
        return self.register.get(path)

    def _make_directory(self, directory_name: str) -> Directory:
        new_directory = Directory.create_empty(directory_name, self.working_directory)
        self.register[create_path(new_directory.name, self.working_directory)] = new_directory
        return new_directory

    def create_file_if_not_exist(self, file_name: str, file_size: int):
        if file_name in self.working_directory.files:
            return

        self.working_directory.add_file(File(file_name, file_size))


def create_path(directory_name: str, parent: Optional[Directory]) -> str:
    if parent is None:
        return directory_name

    if parent.name == Directory.ROOT:
        return f'{parent.name}{directory_name}'

    return f'{create_path(parent.name, parent.parent)}/{directory_name}'
