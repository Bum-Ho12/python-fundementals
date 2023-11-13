'''file that defines a basic monad'''
from __future__ import annotations
from typing import Callable,TypeVar,Generic,Optional

T = TypeVar("T")
U = TypeVar("U")

class Maybe(Generic[T]):
    '''Maybe class that defines a basic monad'''
    def __init__(self, value: Optional[T]) -> None:
        self.value = value

    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[T] | Maybe[U]:
        '''a bind function'''
        return self if self.value is None else func(self.value)

def safe_divide(x: float, y: float) -> Maybe[float]:
    '''divider'''
    return Maybe(None) if y == 0 else Maybe(x/y)

def main() -> None:
    '''main function'''
    result = (
        Maybe(10).bind(lambda x: safe_divide(x,0)).bind(lambda x: safe_divide(x,2))
    )
    print(result.value)

if __name__ == '__main__':
    main()
