__version__ = '0.0.3'


def eat(*ex, **kwargs):
    error_handler = kwargs.get('error_handler', None)
    error_value = kwargs.get('error_value', None)

    def inner(func):
        def wrapper(*args, **kw):
            try:
                return func(*args, **kw)
            except ex as e:
                if error_handler is not None:
                    return error_handler(e, *args, **kw)
                return error_value

        return wrapper

    return inner
