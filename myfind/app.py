import argparse
from pathlib import Path
from .models import ObjectType


def calculate_object_equals_type_all(args):
    """
    Вычисление типа объекта по переданному пути
    Добавление пути во множество при равенстве типа с переданным
    :param args:
    Передаются путь для поиска объектов, необходимое имя и тип
    :return:
    Возвращается множество со всеми путями
    """
    new_paths = set()
    for path in Path(args.path).rglob(args.name):
        new_path = ObjectType(path)
        new_path = new_path.object_equal_type(args.type)
        if new_path:
            new_paths.add(new_path)
    return new_paths


def get_args(*args):
    """
    Получение аргументов из командной строки
    :param args:
    Получение аргументов из тестов
    :return:
    Возвращает полученные аргументы
    """
    parser = argparse.ArgumentParser(description="Myfind")
    parser.add_argument("path", action="store", help="Path")
    parser.add_argument(
        "-name", action="store", dest="name", help="Pattern of filename", default="*"
    )
    parser.add_argument(
        "-type", action="store", dest="type", help="File or directory", default="*"
    )
    return parser.parse_args(*args)


def get_good_objects(*args):
    """
    Получение аргументов и объектов удовлетворяющих аргументам
    :param args:
    Получение аргументов из тестов
    :return:
    Возвращение объектов удовлетворяющих аргументам
    """
    args = get_args(*args)
    good_objects = calculate_object_equals_type_all(args)
    return good_objects


def main(*args, test=False):
    """
    Вывод на экран объектов удовлетворяющих аргументам
    :param args:
    Аргументы для теста
    :param test:
    Проводится ли тест
    """
    good_objects = get_good_objects(*args)
    for obj in good_objects:
        print(obj)
    if test:
        return good_objects
    return None
