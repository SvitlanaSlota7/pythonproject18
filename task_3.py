from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # bool: якщо рядок "True"/"False", обробляємо їх окремо
            if isinstance(result, str):
                if result.lower() == 'true': return True
                if result.lower() == 'false': return False
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

# Тести
assert do_nothing('25') == 25
assert do_something('True') is True
assert do_something('False') is False

print("Результат do_nothing('25'):", do_nothing('25'), type(do_nothing('25')))
print("Результат do_something('True'):", do_something('True'), type(do_something('True')))