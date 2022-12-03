from logging import getLogger


def logger(f):
    def func(*args, **kwargs):
        getLogger().info(f' {args[0]._class_name} => {args[0]._function_name} => {f.__name__}')
        return f(*args, **kwargs)

    return func
