####PYTHON ALMOST A CIRCLE
Square
Represents a square. Inherits from Rectangle with:

Class constructor def __init__(self, size, x=0, y=0, id=None):
The width and height of the Rectangle superclass are assigned using the value of size.
Overwrite of __str__ method to print a Square instance in the format [Square] (<id>) <x>/<y>.
Public method def update(self, *args, **kwargs): that updates an instance of a Square with the given attributes.
*args must be supplied in the following order:
1st: id
2nd: size
3rd: x
4th: y
**kwargs is expected to be a double pointer to a dictoinary of new key/value attributes to update the Square with.
**kwargs is skipped if *args exists.
Public method def to_dictionary(self): that returns the dictionary representation of a Square.
