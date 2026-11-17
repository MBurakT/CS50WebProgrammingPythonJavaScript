# from 09functions import square
import importlib

functions = importlib.import_module("09functions")

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
