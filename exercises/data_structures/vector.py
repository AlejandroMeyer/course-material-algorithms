"""
Vector Classes - Object-Oriented Programming Exercise

Implement vector classes with operator overloading and inheritance.
"""

import math

class Vector:
    """Base Vector class with x, y, z coordinates."""
    
    def __init__(self, x, y, z):
        """
        Initialize a vector with x, y, z coordinates.
        
        Args:
            x: x-coordinate
            y: y-coordinate
            z: z-coordinate
        """
        # TODO: Initialize the vector coordinates
        pass

    def __add__(self, other):
        """
        Overload the addition operator to add two vectors.
        
        Args:
            other (Vector): Another vector to add
            
        Returns:
            Vector: A new vector representing the sum
        """
        # TODO: Implement vector addition
        pass

    def magnitude(self):
        """
        Calculate the magnitude (length) of the vector.
        
        Returns:
            float: The magnitude of the vector
        """
        # TODO: Implement magnitude calculation
        # Hint: magnitude = sqrt(x^2 + y^2 + z^2)
        pass

class Vector3D(Vector):
    """Extended Vector class with additional methods."""
    
    def dot_product(self, other):
        """
        Calculate the dot product of this vector with another vector.
        
        Args:
            other (Vector3D): Another vector
            
        Returns:
            float: The dot product
        """
        # TODO: Implement dot product
        # Hint: dot_product = x1*x2 + y1*y2 + z1*z2
        pass

    def __str__(self):
        """
        Return a string representation of the vector.
        
        Returns:
            str: String in format "(x, y, z)"
        """
        # TODO: Implement string representation
        pass
