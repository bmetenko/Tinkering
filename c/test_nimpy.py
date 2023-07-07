# test.py
import test_nimpy as mymodule
assert mymodule.greet("world") == "Hello, world!"
assert mymodule.greet(name="world") == "Hello, world!"

print("Passed all tests here...")
print(f"{mymodule.greet(name='world')=}")