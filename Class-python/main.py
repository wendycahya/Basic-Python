import custom as cm
import math
#Use the Person class to create an object, and then execute the printname method:

cls = cm.Person("Wendy", "Cahya")

# cls.name_user("Wendy", "Cahya")
cls.printname()

in_array = [0, math.pi/2, math.pi/3, math.pi]

a = cls.cos_function(in_array)

print(a)