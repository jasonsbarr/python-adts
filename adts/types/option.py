from ..variant import Variant
from ..decorators import curry
from typing import TypeVar, TypeAlias, Union, Callable
from types import NoneType

T = TypeVar("T")
T2 = TypeVar("T2")

# type Option
# | Some[T]
# | None

# superclass for defining shared special methods


class Optional(Variant[T]):
    def __init__(self):
        if self.__class__ == Optional:
            raise TypeError("Cannot instantiate Optional class directly")

    # Setoid
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

    # Ord
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

    # SemiGroup
    def __add__(self, other):
        if not isinstance(other, Optional):
            raise TypeError("Can only add an Option to another Option")

        match self:
            case Some() if not self.value is None:
                match other:
                    case Some(value):
                        return Some(self.value + value)
                    case Nothing():
                        return other
            case Some() if self.value is None:
                return other
            case Nothing():
                return self


class Some(Optional[T]):
    def __str__(self):
        return f"Some({self.value})"

    def __repr__(self):
        return str(self)


class Nothing(Optional[NoneType]):
    def __str__(self):
        return "Nothing"

    def __repr__(self):
        return str(self)


Option: TypeAlias = Union[Some[T], Nothing]

# Functor


@curry
def map(fn: Callable[[T], T2], opt: Option):
    match opt:
        case Some():
            return of(fn(opt.value))
        case Nothing():
            return opt

# Monoid


def empty():
    return Some()

# Monad


def of(value: Union[T, NoneType]) -> Option:
    return Nothing() if value == None else Some(value)


@curry
def bind(fn: Callable[[Option], Option], opt: Option):
    match opt:
        case Some():
            return fn(opt.value)
        case Nothing():
            return opt
