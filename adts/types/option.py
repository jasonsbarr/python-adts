from ..variant import Variant
from typing import TypeVar, TypeAlias, Union, Callable
from types import NoneType

T = TypeVar("T")

# type Option
# | Some[T]
# | None


class Some(Variant[T]):
    pass


class Nothing(Variant[NoneType]):
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
