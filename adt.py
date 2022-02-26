from abc import ABC
from typing import Any
import inspect
import sys

class ADT(ABC):
    pass

# set the __value__ property on an instance without its own fields
def set_instance_value(instance, args):
    if len(args) == 1:
        setattr(instance, "value", args[0])
    elif len(args) > 1:
        setattr(instance, "value", args)


# variants is a list of dictionaries that match the one returned by create_variant
# members are data attributes and methods, including dunder methods, to be attached to the type representative
# do not include variant names as method names, as these will be created as methods on the type representative
# global_constructors=True creates a separate class in the calling module for each variant
# typeclasses are abstract classes that provide functions you must define on the type representative in members
def create_adt(type_name, *, variants=None, members=None, global_constructors=True, typeclasses=None):
    if members is None:
        members = {}

    members["__variants__"] = []

    if not "__init_subclass__" in members:
        def init_subclass(cls):
            base_class = cls.__bases__[0]
            if not hasattr(base_class, "__variants__"):
                base_class.__variants__ = []

            base_class.__variants__.append(cls)
            setattr(base_class, cls.__name__, cls)

        members["__init_subclass__"] = init_subclass

    if variants is None:
        if not "__init__" in members:
            def init(self, *args):
                set_instance_value(self, args)
                setattr(self, "__type__", self)

            members["__init__"] = init

    supers = [ADT]

    if not typeclasses is None:
        for tc in typeclasses:
            supers.append(tc)


    tyrep = type(type_name, tuple(supers), members)

    if not variants is None:
        for variant in variants:
            var = type(variant["name"], (tyrep,), variant["members"])

            # this is a fucking terrible idea and I probably shouldn't do it
            if global_constructors:
                current_frame = inspect.currentframe()
                calling_module = sys.modules[current_frame.f_back.f_globals['__name__']]
                gs = calling_module.__dict__
                gs[variant["name"]] = var

    return tyrep



# fields is a list with field names (strings)
# members are data attributes and methods, including dunder methods, to be attached to the instance
# you should either provide a list of fields OR an __init__ method in members, not both
# positional arguments passed into a variant's constructor call MUST be in the same order as they are in this fields list
def create_variant(variant_name, *, fields=None, members=None):
    if members is None:
        members = {}

    if not "__init__" in members:
        def init(self, *args, **kwargs):
            if not fields is None:
                for k, v in kwargs.items():
                    setattr(self, k, v)

                for i, v in enumerate(args):
                    setattr(self, fields[i], v)

            else:
                set_instance_value(self, args)

            setattr(self, "__type__", self.__class__)
            setattr(self, "__variant__", self)

        members["__init__"] = init

    return {"name": variant_name, "members": members}
