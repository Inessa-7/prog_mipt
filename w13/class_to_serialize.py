import json


class MyClass:
    def __init__(self, name, surname, is_hired):
        self.name = name
        self.surname = surname
        self.is_hired = is_hired


def obj_to_json(my_class_instance):
    """
    Получает на вход объект класса MyClass,
    выдает на выходе JSON-представление.

    >>> a = MyClass('me', 'my_surname', True)
    >>> obj_to_json(a)
    {'name': 'me', 'surname': 'my_surname', 'is_hired': True'}
    """
    # NOTE: используйте obj.__dict__, не пишите явно все поля класса
    return json.dumps(my_class_instance.__dict__)


def json_to_obj(my_class_instance):
    """
    Получает на вход JSON-представление,
    выдает на выходе объект класса MyClass.

    >>> a = MyClass('me', 'my_surname', True)
    >>> json_dict = get_json(a)
    >>> b = json_to_obj(json_dict)
    <__main__.MyClass object at 0x7fd8e9634510>
    """
    # NOTE: можно использовать kwargs: MyClass(**some_dict)
    return MyClass(**json.loads(my_class_instance))
	

if __name__ == '__main__':
	a = MyClass('me', 'my_surname', True)
	print(obj_to_json(a))
	json_dict = obj_to_json(a)
	b = json_to_obj(json_dict)
	print(b)

