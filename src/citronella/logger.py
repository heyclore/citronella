from logging import getLogger


def logger(f):
    def func(*args, **kwargs):
        getLogger().info(f'{args[0]._name} element {f.__name__}')
        return f(*args, **kwargs)

    return func
