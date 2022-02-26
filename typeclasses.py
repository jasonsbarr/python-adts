from abc import ABC, abstractmethod

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