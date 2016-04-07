__version__ = '0.0.5'


def eat(*ex, **kwargs):
    error_handler = kwargs.get('error_handler', None)
    error_value = kwargs.get('error_value', None)

    def inner(func):
        def wrapper(*args, **kw):
            def caught_it(e):
                """
                Calls the error handler or returns the error value.
                :param e: The caught exception.
                :return: The error value or the result of the error handler.
                """
                if error_handler is not None:
                    return error_handler(e, *args, **kw)
                return error_value

            # default to catching any exception
            exceptions = ex or Exception

            # catch any exception in `exceptions`
            try:
                return func(*args, **kw)
            except exceptions as e:
                return caught_it(e)

        return wrapper

    return inner
