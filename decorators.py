from functools import partial
import inspect

def curry(fn)
    def curried(*args, **kwargs):
        argspec = inspect.getfullargspec(fn)
        all_args_count = len(argspec.args) + len(argspec.kwonlyargs) - len(argspec.kwonlydefaults.keys())

        if all_args_count >= all_args_count:
            return fn(*args, **kwargs)
        return curry(partial(fn, *args, **kwargs))

    return curried

def curry_method(fn)
    def curried(*args, **kwargs):
        argspec = inspect.getfullargspec(fn)
        all_args_count = len(argspec.args) + len(argspec.kwonlyargs) - len(argspec.kwonlydefaults.keys())

        if all_args_count >= all_args_count:
            return fn(*args, **kwargs)
        return curry_method(partial(fn, *args, **kwargs))

    return curried