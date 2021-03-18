import argparse
from pathlib import Path
import pytest
from myfind.app import calculate_object_equals_type_all
from myfind.app import ObjectType
from myfind.app import get_args
from myfind.app import get_good_objects
from myfind.app import main
from myfind.models import PathType

CONTENT = "content"


class Args:
    """
    Имитация аргументов из командной строки
    """

    path = Path("Нужно присвоить tmp_path в функции")
    name = PathType.ALL.value
    type = PathType.ALL.value


def test_get_args(tmp_path):
    """
    Сравнение вычисленных и полученных аргументов
    """
    Args.path = tmp_path
    args = Args
    args_in_app = ObjectType(tmp_path)
    assert args.path.is_dir() == args_in_app.path.is_dir()
    assert args.path == args_in_app.path


def create_file(tmp_path, dirs, files):
    """
    Создание файлов и папок для проверки
    """
    path = tmp_path
    for mydir in dirs:
        path = path / mydir
        path.mkdir()

    for file in files:
        file_path = path / file
        file_path.write_text(CONTENT)


def create_path_to_file(tmp_path, dirs, files):
    """
    Вычисление путей для созданных файлов и папок
    """
    new_list = set()
    path = tmp_path
    for mydir in dirs:
        path = path / mydir
        new_list.add(path)
    for file in files:
        new_list.add(path / file)
    return new_list


@pytest.mark.parametrize(
    ("dirs", "files"),
    [
        (["sub"], ["hello.py", "isfile"]),
        (["grow"], ["hello.txt", "file.txt"]),
        (["grow", "grow"], ["hello.txt", "file.txt"]),
    ],
)
def test_check_path_to_file(tmp_path, dirs, files):
    """
    Сравнение созданных путей с полученными
    """
    create_file(tmp_path, dirs, files)
    check_list = create_path_to_file(tmp_path, dirs, files)
    Args.path = tmp_path
    path = calculate_object_equals_type_all(Args)
    assert path == check_list


def test_call_get_args(mocker, tmp_path):
    """
    Проверка вызова функции получения аргумнтов
    """
    mocker.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(path=tmp_path),
    )
    args = get_args()
    assert args == argparse.Namespace(path=tmp_path)


@pytest.mark.parametrize(
    ("dirs", "files"),
    [
        (["sub"], ["hello.py", "isfile"]),
        (["grow"], ["hello.txt", "file.txt"]),
        (["grow", "grow"], ["hello.txt", "file.txt"]),
    ],
)
def test_default_args(tmp_path, dirs, files):
    """
    Сравнение полученных аргументов со стандартными
    """
    create_file(tmp_path, dirs, files)
    create_path_to_file(tmp_path, dirs, files)
    args = get_args([str(tmp_path)])
    assert args.name == '*'
    assert args.path == str(tmp_path)
    assert args.type == PathType.ALL.value


def test_object_type1(tmp_path):
    """
    Сравнение пути до папки с типом "all"
    """
    mydir = ObjectType(tmp_path)
    new_path = mydir.object_equal_type(PathType.ALL.value)
    assert new_path == tmp_path


def test_object_type2(tmp_path):
    """
    Сравнение пути до папки с типом "None"
    """
    mydir = ObjectType(tmp_path)
    new_path = mydir.object_equal_type("None")
    assert new_path is None


def test_object_type_d(tmp_path):
    """
    Сравнение пути до папки с типом "папка"
    """
    mydir = ObjectType(tmp_path)
    new_path = mydir.object_equal_type(PathType.DIR.value)
    assert new_path == tmp_path


@pytest.mark.parametrize(
    ("dirs", "files"),
    [
        (["sub"], ["hello.py", "isfile"]),
        (["grow"], ["hello.txt", "file.txt"]),
        (["grow", "grow"], ["hello.txt", "file.txt"]),
    ],
)
def test_main(tmp_path, dirs, files):
    """
    Сравнение созданных путей с полученными путями из main
    """
    create_file(tmp_path, dirs, files)
    create_path_to_file(tmp_path, dirs, files)
    good_objects = get_good_objects([str(tmp_path)])
    assert good_objects == main([str(tmp_path)], test=True)
