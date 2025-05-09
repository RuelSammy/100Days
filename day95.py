#Explore advanced topics like metaclasses.
class InterfaceMeta(type):
    def __new__(cls, name, bases, dct):
        if "run" not in dct:
            raise TypeError(f"Class {name} must implement a 'run' method")
        return super().__new__(cls, name, bases, dct)

class Job(metaclass=InterfaceMeta):
    def run(self):
        print("Running job")

# This will raise an error
class IncompleteJob(metaclass=InterfaceMeta):
    pass
