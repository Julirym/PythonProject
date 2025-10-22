def function_logs(func):
    def wrapper(*args, **kwargs):
        print('------------')
        print(f"Вызывается функция с аргументами: {args}, {kwargs}")

        result = func(*args, **kwargs)

        print(f"Результат работы функции: {result}")
        print('------------\n')

        return result

    return wrapper


def add_smile(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return f"{result} 😎"

    return wrapper