import numpy as np


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def cos_function(self, array):
        cos_value = np.cos(array)
        print("\n Cosine values: \n", cos_value)
        return cos_value


