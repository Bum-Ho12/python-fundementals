'''
file that describe the applications of Functors
'''
from __future__ import annotations

from typing import Any, Callable

class Functor:
    '''class that defines a functor'''
    def __init__(self,value: Any) -> None:
        self.value =value

    def map(self, func: Callable[[Any],Any]) -> Functor:
        '''function that performs functor operation'''
        return Functor(func(self.value))

def add_one(x:int) -> int:
    '''function that one to a number'''
    return x+ 1

def multiply_by_two(x: int) -> int:
    '''function multiplies number by two'''
    return x*2

def main() -> None:
    '''main function'''
    f = Functor(5)

    # Mapping within the same category (Functor -> Functor)
    g = f.map(add_one) # g is also a Functor instance

    # Preserving structure
    assert isinstance(g, Functor)

    # Preserving composition
    assert(
        f.map(add_one).map(multiply_by_two).value
        == f.map(lambda x: multiply_by_two(add_one(x))).value
    )

if __name__ == '__main__':
    main()
