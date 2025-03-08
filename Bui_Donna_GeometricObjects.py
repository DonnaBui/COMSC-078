# Object-oriented Program - Donna Bui - 3/30/2023 - Professor Henry Estrada's COMSC 078
# This program will create a Circle and Rectangle object from the GeometricObject class and print out each shape's properties.

import datetime
import math

""" GeometricObject class containing methods and constructors for a standard shape object """
class GeometricObject:
    
    defaultColor = "Blue"
    defaultFilled = True
    
    def __init__(self, color = defaultColor, filled = defaultFilled): 
        self.color = str(color) if color is not None else self.defaultColor
        self.filled = bool(filled) if filled is not None else self.defaultFilled
        self.dateCreated = datetime.date.today()
        
    def setColor(self, color): # Setter for changing color
        self.color = str(color)
        
    def getColor(self): # Getter for getting the color
        return self.color
    
    def setFilled(self, filled): # Setter for Fill boolean
        self.filled = bool(filled)
        
    def isFilled(self): # Getter to return whether or not the object is filled
        return self.filled
    
    def getDateCreated(self): # Getter to return the date object was created
        return self.dateCreated
    
    # Returns the object's type, if not a specific class (e.g. Circle or Rectangle), then it will simply be GeometricObject, followed by the shape's color, fill status, and date created.
    def __str__(self): 
        return("Shape: " + type(self).__name__ + "\nDate Created: " + str(self.dateCreated) + "\nColor: " + self.color + "\nFilled: " + str(self.filled))
    
    
"""  Circle class inheriting GeometricObject. Contains additional constructors for circle-specific properties such as Radius. """
class Circle(GeometricObject): 
    
    # Parameterized constructor - Has default values and takes parameters for Radius, Color, and Filled status.
    def __init__(self, radius = 1, color = GeometricObject.defaultColor, filled = GeometricObject.defaultFilled): 
        self.radius = abs(float(radius)) if radius is not None else 1
        GeometricObject.__init__(self, color, filled) 
    
    def setRadius(self, radius): # Setter for changing radius
        self.radius = abs(float(radius)) if radius is not None else 1
        
    def getRadius(self): # Getter for getting the radius
        return self.radius
    
    def getArea(self): # Getter to calculate Area of the circle (pi * radius^2)
        return (math.pi)*(self.radius)**2
    
    def getPerimeter(self): # Getter to calculate the perimeter of the circle ( 2 * pi * radius)   
        return 2*(math.pi)*(self.radius)
    
    def __str__(self): # Calls the inherited __str__ function from GeometricObject to get the basic information, then combines that with the Radius, Area, and Perimeter
        return (GeometricObject.__str__(self) + "\nRadius: " + str(self.radius) + "\nArea: " + str(self.getArea()) + "\nPerimeter: " + str(self.getPerimeter()))


""" Rectangle class inheriting GeometricObject. Contains additional constructors for shape-specific properties such as Length and Width. """
class Rectangle(GeometricObject):
    
    def __init__(self, width = 1, height = 1, color = GeometricObject.defaultColor, filled = GeometricObject.defaultFilled): # Parameterized constructor with default values
        self.width = abs(float(width)) if width is not None else 1
        self.height = abs(float(height)) if height is not None else 1
        GeometricObject.__init__(self, color, filled) 
    
    def setWidth(self, width): # Setter for width
        self.width = abs(float(width)) if width is not None else 1
    
    def getWidth(self): # Getter for width
        return self.width
    
    def setHeight(self, height): # Setter for height
        self.height = abs(float(height)) if height is not None else 1
    
    def getArea(self): # Returns the area (width * height)
        return (self.height * self.width)
    
    def getPerimeter(self): # Returns the perimeter (height + width) * 2
        return (self.height + self.width) * 2
    
    def __str__(self): # Utilizes inherited __str__ method and prints out the Width, Height, Area, and Perimeter
        return (GeometricObject.__str__(self) + "\nWidth: " + str(self.width) + "\nHeight: " + str(self.height) + "\nArea: " + str(self.getArea()) + "\nPerimeter: " + str(self.getPerimeter()))

""" Driver Method"""
def main():
    radius = input("Enter the radius of your circle: ")
    print()
    
    circle = Circle(radius) # Creates a circle using the user-provided radius. Automatically applies default values for Color and Filled (Blue and True).
    print(circle, "\n")

    rectangle = Rectangle(2, 2, "Pink", False) # Typical rectangle with all parameters provided
    rectangle.setColor("Red")
    print(rectangle, "\n")
    
    """
    # -----------------------------------------------
    # Additional code for testing
    # -----------------------------------------------
    circle2 = Circle(2, "Red", False) 
    print("Circle2", circle2, "\n") # Color: Red, Filled: False, Radius: 2
    
    circle3 = Circle(-5, None, True)
    print("Circle3", circle3, "\n") # Blue, True, 5
    
    circle4 = Circle(None, "Purple")
    print("Circle4", circle4, "\n") # Purple, True, 1
    
    circle5 = Circle()
    print("Circle5", circle5, "\n") # Blue, True, 1
    
    circle5.setRadius(-5)
    circle5.setColor("Red")
    print("New Circle5", circle5, "\n") # Red, True, 5
    # -----------------------------------------------
    geoObj1 = GeometricObject()
    print("geoObj1", geoObj1, "\n") # Color: Blue, Filled: True
    
    geoObj2 = GeometricObject("Green", False)
    print("geoObj2", geoObj2, "\n") # Green, False
    
    geoObj3 = GeometricObject("Red") 
    print("geoObj3", geoObj3, "\n") # Red, True
    
    geoObj4 = GeometricObject(None, False) 
    print("geoObj4", geoObj4, "\n") # Blue, False
    # -----------------------------------------------
    rectangle2 = Rectangle()
    print("rectangle2", rectangle2, "\n") # Width: 1, Height: 1, Color: Blue, Filled: True
    
    rectangle3 = Rectangle(None, None, "Orange")
    print("rectangle3", rectangle3, "\n") # 1, 1, Orange, True
    
    rectangle4 = Rectangle(-2, 2)
    print("rectangle4", rectangle4, "\n") # 2, 2, Blue, True
    
    rectangle4.setHeight(-10)
    rectangle4.setFilled(False)
    print("New rectangle4", rectangle4, "\n") # 2, 10, Blue, False
    # -----------------------------------------------
    """
    
main()