from typing import Any

def hasmethod(obj: Any, meth: str) -> bool:
    hasattr(obj, meth) and callable(getattr(obj, meth))

py_map = map

def map(fn, data):
    if hasattr(data, "__type__") and hasmethod(data.__type__, "map"):
        return data.__type__.map(fn, data)

    return py_map(fn, data)

def compose2(f, g):
    return lambda x: g(f(x))

def compose(*fns):
    acc = lambda x: x
    for fn in fns:
        acc = compose2(fn, acc)
    return acc

def pipe(val, *fns):
    return compose(*fns)(val)
