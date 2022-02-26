from abc import ABC
from typing import Any

class ADT(ABC):
    def __setattr__(self):
        raise ValueError("Cannot set values on an ADT instance")

    def __delattr__(self):
        raise ValueError("Cannot delete values on an ADT instance")

# set the __value__ property on an instance without its own fields
def set_instance_value(instance, *args):
    if len(args) == 1:
        setattr(instance, "__value__", args[0])
    elif len(args) > 1:
        setattr(instance, "__value__", args)

    @property
    def _get_value(self):
        return self.__value__

    setattr(instance, value, _get_value)


# variants is a list of dictionaries that match the one returned by create_variant
# members are data attributes and methods, including dunder methods, to be attached to the type representative
# do not include variant names as method names, as these will be created as methods on the type representative
def create_adt(type_name, *, variants=None, members=None):
    if members is None:
        members = {}

    members["__variants__"] = []

    if not "__init_subclass__" in members:
        def init_subclass(cls):
            base_class = cls.__bases__[0]
            if not hasattr(base_class, "__variants__");
                base_class.__variants__ = []

            base_class.__variants__.append(cls)
            setattr(base_class, cls.__name__, cls)

        members["__init_subclass__"] = init_subclass

    if variants is None:
        if not "__init__" in members:
            def init(self, *args):
                set_instance_value(self, args)

            members["__init__"] = init

    tyrep = type(type_name, (ADT,), members)

    if variants not None:
        gs = globals()
        for variant in variants:
            gs[variant["name"]] = type(variant["name"], (tyrep,), variant["members"])

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
            if fields not None:
                for k, v in kwargs.items():
                    setattr(self, k, v)

                for i, v in enumerate(args):
                    setattr(self, fields[i], v)

            else:
                if len(args) == 1:
                    setattr(self, "__value__", args[0])
                elif len(args) > 1:
                    setattr(self, "__value__", args)

        members["__init__"] = init

    return {"name": variant_name, "members": members}
