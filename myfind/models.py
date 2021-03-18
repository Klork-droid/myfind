from enum import Enum


class PathType(Enum):
    DIR = 'd'
    FOLDER = 'F'
    ALL = '*'


class ObjectType:
    """
    Вычисление переданному пути типа объекта
    Сравнение типа объекта с типом из аргументов
    """

    def __init__(self, path):
        self.path = path
        self.type = self.init_type()

    def init_type(self):
        path_type = PathType.DIR.value if self.path.is_dir() else PathType.FOLDER.value
        return path_type

    def object_equal_type(self, object_type):
        if object_type in (PathType.ALL.value, self.type):
            return self.path
        return None
