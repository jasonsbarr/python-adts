from ..variant import Variant
from typing import TypeVar, TypeAlias, Union
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
