from dataclasses import dataclass, astuple
from typing import TypeVar, Generic
from abc import ABC

T = TypeVar("T")


@dataclass
class Variant(ABC, Generic[T]):
    def __new__(cls):
        if cls == Variant:
            raise TypeError("Cannot instantiate Variant class directly")

        return super().__new__(cls)

    def __init__(self, value=None):
        self.__dict__["_value"] = value

    @property.getter
    def value(self):
        return self._value

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise ValueError("Cannot change values on a Variant type")

    def __iter__(self):
        return iter(astuple(self.value))
