def same_type(func):
    def wrapper(*args, **kwargs):
        if args and len({type(args) for args in args}) > 1:
            print("Обнаружены различные типы данных")
            return

        return func(*args, **kwargs)

    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
