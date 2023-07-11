# test.py
import test_nimpy as mymodule
assert mymodule.greet("world") == "Hello, world!" # type: ignore
assert mymodule.greet(name="world") == "Hello, world!" # type: ignore

print("Passed all tests here...")
print(f"{mymodule.greet(name='world')=}") # type: ignore


print(f"{mymodule.check_py_call()}") # type: ignore


t1 = (1,2)
t2 = (3,4)

print(f"{mymodule.tuple_diff(t1, t2)}") # type: ignore

import timeit

a = timeit.timeit("""
mymodule.tuple_diff(t1, t2)
""", number=10000, setup='import test_nimpy as mymodule; t1 = (1,2); t2 = (3,4);')

b = timeit.timeit("""
(t1[i] - t2[i] for i in range(2))
""", number=10000)

print(f"{a=}, {b=}")

print(mymodule.nim_json()) # type: ignore