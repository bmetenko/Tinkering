import importlib
import inspect

def get_callables_from_package(package):

    # Get all members (functions, classes, etc.) of the package
    members = dir(package)

    # Filter callable objects (functions and classes) and create a dictionary
    callables_dict = {}
    for member in members:
        obj = getattr(package, member)
        if callable(obj):
            callables_dict[member] = obj

    return callables_dict