from os.path import dirname, join

from setuptools import find_packages, setup

setup(
    name='Myfind',
    description='Myfind',
    version='1.0',
    author='Kirill Dyukin',
    author_email='example@gmail.com',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={'console_scripts': ['myapp = myapp.app:main']},
)
