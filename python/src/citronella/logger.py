from logging import info


def logger(f):
    def func(*args, **kwargs):
        if args[0]._logger:
            info(f'{args[0]._class_name} => '
                 '{args[0]._function_name} => {f.__name__}')
        return f(*args, **kwargs)

    return func
