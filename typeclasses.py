from abc import ABC, abstractmethod

class Setoid(ABC):
    @classmethod
    @abstractmethod
    def eq(cls, instance, other)

    def __eq__(self, other):
        return self.__class__.eq(self, other)

    def __ne__(self, other):
        return not self.__class__.eq(self, other)

class Ord(Setoid):
    @classmethod
    @abstractmethod
    def le(cls, instance, other)

    def __le__(self, other):
        return self.__type__.le(self, other)

    def __gt__(self, other):
        return not self.__type__.le(self, other)

    def __ge__(self, other):
        return not self.__type__.le(self, other) and not self.__type__.eq(self, other)

    def __lt__(self, other):
        return not self.__ge__(self, other)


class Functor(ABC):
    @classmethod
    @abstractmethod
    def map(cls, fn, instance)

class Applicative(Functor)
    @classmethod
    @abstractmethod
    def ap(cls, instance, other)

class SemiGroup(ABC):
    @classmethod
    @abstractmethod
    def concat(cls, instance, other)


    def __add__(self, other):
        return self.__type__.concat(self, other)

class Monoid(SemiGroup):
    @classmethod
    @abstractmethod
    def empty(cls)

class Monad(Functor, Monoid):
    @classmethod
    @abstractmethod
    def chain(cls, fn, instance)

    @classmethod
    @abstractmethod
    def of(cls, value)

class Fold(Functor):
    @classmethod
    @abstractmethod
    def fold(cls, fn, instance)