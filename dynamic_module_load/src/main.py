import os
import importlib
import inspect


def parse():
    package_name = 'parser'
    parser_dir = os.listdir(package_name)
    skip_class_name = ['__init__.py', 'base_parser.py']

    for file_name in parser_dir:
        if file_name.endswith('py') and \
                file_name not in skip_class_name:
            module_name = os.path.splitext(file_name)[0]
            classpath = package_name + '.' + module_name
            parser = importlib.import_module(classpath)
            clazz_list = inspect.getmembers(parser, inspect.isclass)

            for clazz in clazz_list:
                if clazz[0] != 'BaseParser':
                    instance = clazz[1]()
                    instance.parse()


if __name__ == '__main__':
    parse()
