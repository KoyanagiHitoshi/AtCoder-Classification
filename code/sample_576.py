from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)


print(fibonacci(100))
