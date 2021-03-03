class ObjectType:
    """
    Вычисление переданному пути типа объекта
    Сравнение типа объекта с типом из аргументов
    """

    def __init__(self, path):
        self.path = path
        self.type = self.init_type()

    def init_type(self):
        path_type = "dir" if self.path.is_dir() else "file"
        return path_type

    def object_equal_type(self, object_type):
        if object_type in ("*", self.type):
            return self.path
        return None
