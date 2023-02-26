from logging import info


def logger(f):
    """This is a logger wrapper."""
    def func(*args, **kwargs):
        """This is a logger method."""
        if args[0]._logger:
            info(f'{args[0]._class_name} => '
                 f'{args[0]._function_name} => {f.__name__}')
        return f(*args, **kwargs)

    return func
