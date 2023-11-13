'''file that implements maybe monad with match pattern'''
from __future__ import annotations
from typing import Generic, Optional, TypeVar, Callable

T = TypeVar("T")
U = TypeVar("U")

class Maybe(Generic[T]):
    '''maybe class monad'''
    def __init__(self,value: Optional[T]) -> None:
        self.value = value

    def bind(self, func: Callable[[T],Maybe[U]]) -> Maybe[T] | Maybe[U]:
        '''bind function'''
        return self if self.value is None else func(self.value)

    __match_args__ = ("value",)

    def __match__(self, other: Maybe[T]) -> bool:
        return self.value ==other.value

def parse_int(value: str) -> Maybe[int]:
    '''function that converts string to int'''
    try:
        return Maybe(int(value))
    except ValueError:
        return Maybe(None)

def is_positive(value: int) -> Maybe[int]:
    '''function that checks if value is +ve'''
    return Maybe(value) if value > 0 else Maybe(None)

def double(value: int) -> int:
    '''function that doubles a number'''
    return value * 2

# Validate and process user input
def validate_and_process(input_str: str) -> Maybe[str] | Maybe[int]:
    '''function that validates an input'''
    return(
        Maybe(input_str)
        .bind(parse_int)
        .bind(is_positive)
        .bind(lambda n: Maybe(double(n)))
    )



def main() -> None:
    '''main function'''
    # Example inputs
    inputs = ["5","-3","foo"]

    # Process inputs
    for input_str in inputs:
        print(f"Processing '{input_str}': ")
        result = validate_and_process(input_str)
        match result:
            case Maybe(None):
                print(f"Invalid input: {input_str}!")
            case Maybe(value= int()):
                print(f"Result: {result.value}")
            case _:
                print("Unexpected input!")
    print("Done!")

if __name__ == "__main__":
    main()
