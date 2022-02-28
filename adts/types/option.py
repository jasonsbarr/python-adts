from ..variant import Variant
from typing import TypeVar, TypeAlias, Union, Callable
from types import NoneType

T = TypeVar("T")

# type Option
# | Some[T]
# | None

# superclass for defining shared special methods


class Optional(Variant[T]):
    def __init__(self):
        if self.__class__ == Optional:
            raise TypeError("Cannot instantiate Optional class directly")

    def __eq__(self, other):
        match self:
            case Some():
                match other:
                    case Some(value):
                        return self.value == value
                    case _:
                        return False
            case Nothing():
                match other:
                    case Nothing():
                        return True
                    case _:
                        return False

    def __le__(self, other):
        match self:
            case Some():
                match other:
                    case Some(value):
                        return self.value <= value
                    case _:
                        return False
            case Nothing():
                match other:
                    case Nothing():
                        return True
                    case _:
                        return False

    def __lt__(self, other):
        match self:
            case Some():
                match other:
                    case Some(value):
                        return self.value < value
                    case _:
                        return False
            case _:
                return False

    def __gt__(self, other):
        match self:
            case Some():
                match other:
                    case Some(value):
                        return self.value > value
                    case _:
                        return False
            case _:
                return False

    def __ge__(self, other):
        match self:
            case Some():
                match other:
                    case Some(value):
                        return self.value >= value
                    case _:
                        return False
            case Nothing():
                match other:
                    case Nothing():
                        return True
                    case _:
                        return False


class Some(Optional[T]):
    pass


class Nothing(Optional[NoneType]):
    pass


Option: TypeAlias = Union[Some[T], Nothing]


def of(value: Union[T, NoneType]) -> Option:
    return Nothing() if value == None else Some(value)


def map(fn: Callable[[Option], Option], opt: Option):
    match opt:
        case Some():
            return of(fn(opt.value))
        case Nothing():
            return opt
