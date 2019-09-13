from functools import reduce

def pipe(*functions):
    def wrapper(value):
        return reduce(lambda acc, curr : curr(acc), functions, value)

    return wrapper

def identity_func(x):
    return x

def partial_map(func):
    """
    Return an function that map an iterator to the gived func.
    """
    def wrapper(iter):
        return map(func, iter)
    
    return wrapper

def conditional(cond, func1, func2):
    return func1 if cond else func2