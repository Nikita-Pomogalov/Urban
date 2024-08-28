# from pprint import pprint
#
#
# def introspection_info(obj):
#
#     return {'type': type(obj).__name__, 'attributes': dir(obj), 'methods': dir(obj)}
#
#
# pprint(introspection_info(2))

import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = getattr(obj, '__module__', '__main__')

    is_class = inspect.isclass(obj)

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'is_class': is_class,
    }


# Пример использования
number_info = introspection_info(Exception)
print(number_info)