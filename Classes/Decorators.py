'''
Требуется реализовать на языке Python функции-декораторы.

Декоратор counter_decorator возвращает функцию, печатающую в консоль количество вызовов Function calls count: {n} и возвращающую результат декорируемой функцию от переданных аргументов.

Декоратор projection_decorator возвращает функцию 3-х аргументов x,y,z, которая возвращает результат декорируемой функции от аргумента 3x−7y+15z+18.


from typing import Callable

def counter_decorator(f: Callable) -> Callable:
    Decorates `f` to print number of calls each call.
    pass

def projection_decorator(f: Callable[[int], None]) -> Callable[[int, int, int], None]:
    Decorates `f` as a function of three arguments x, y, z that calls `f` with a single argument $3x-7y+15z+18$
    pass
'''

from typing import Callable

def counter_decorator(f: Callable):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print("Function calls count:", wrapper.count)
        f(*args, **kwargs)
    wrapper.count = 0
    return wrapper

def projection_decorator(f: Callable[[int], None]) -> Callable[[int, int, int], None]:
    def wrapper(x, y, z):
        return f(3 * x - 7 * y + 15 * z + 18)
    return wrapper

def sum(a: int, b: int):
    print(a + b)

fn = counter_decorator(sum)
fn(1, 2)
fn(4, 5)
fn(-4, 5)


@projection_decorator

def calc(x: int):
    print(x * x)

calc(1, 2, 3)
