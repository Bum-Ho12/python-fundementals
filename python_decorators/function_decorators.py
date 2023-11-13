import logging
# from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter
from typing import Any, Callable
import functools

logger = logging.getLogger('my_app')


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number))+ 1):
        if number % element == 0:
            return False
    return True

def benchmark( func: Callable[...,Any]) -> Callable[...,Any]:
    @functools.wraps(func) # helps the function to refer to the wrapped functions
    def wrapper(*args: Any, **kwargs: Any) -> Any: # Any takes any kind of args passed through
        start_time = perf_counter() # registers the time
        value = func(*args, **kwargs) # calls counter_prime_numbers function and pass the upper_bound as args
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f" Execution of {func.__name__} took {run_time:.2f} seconds"
        )
        return value
    return wrapper


## The original setup before including the decorator acceptance info

# def with_logging( func: Callable[...,Any]) -> Callable[...,Any]:
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#         logging.info(f"calling {func.__name__}")
#         value = func(*args, **kwargs)
#         logging.info(f"Finished calling {func.__name__}")
#         return value
#     return wrapper


def with_logging( func: Callable[...,Any],logger: logging.Logger) -> Callable[...,Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info(f"calling {func.__name__}")
        value = func(*args, **kwargs)
        logger.info(f"Finished calling {func.__name__}")
        return value
    return wrapper


with_default_logging = functools.partial(with_logging, logger= logger)

@with_default_logging
@benchmark
def counter_prime_numbers( upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count +=1
    return count


def main() -> None:
    logging.basicConfig(level= logging.INFO)
    value = counter_prime_numbers(100000)
    logging.info(f" Number prime numbers: {value}")

if __name__ == '__main__':
    main()

