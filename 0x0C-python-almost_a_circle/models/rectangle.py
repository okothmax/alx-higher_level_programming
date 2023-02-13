#!/usr/bin/python3
'''
import the parent class(Base)
'''
from base import Base

'''
create the child class from the parent class (Base)
'''


class Rectangle(Base):
    '''
    Using the super() to inherit the class attributes of the 'Base' class
    Creating private attributes width, height, x and y

    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(
            id
        )
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' get the width '''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''set the width property
        Raises a TypeError if width is not an integer
        Raises a ValueError if width is less than or equal to zero
        '''
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        ''' get the height '''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''set the height property
        Raises a TypeError if height is not an integer
        Raises a ValueError if height  is less than or equal to zero
        '''
        if not isinstance(value, int):
            raise TypeError('Height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' get x'''
        return self.__x
    
    @x.setter
    def x(self, value):
        '''set x property
        Raises a TypeError if x is not an integer
        Raises a ValueError if x is less than zero
        '''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        ''' get y '''
        return self.__y
    
    @y.setter
    def y(self, value):
        '''set the y property
        Raises a TypeError if y is not an integer
        Raises a ValueError if y is less than zero
        '''
        if type(value) != int:
            raise TypeError('Y must be an integer')
        self.__y = value

    def area(self):
        if self.height == 0 or self.width == 0:
            return
        return self.height * self.width
    
    def display(self):
        if self.__height == 0 or self.__width == 0:
            print("")
            return
        representation_x = []
        symbol = '#'

        [print("") for y in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            for j in range(self.__width):
                representation_x.append(symbol)
            if i != (self.__height - 1):
                representation_x.append('\n')

        return (''.join(representation_x))
    
    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'
        
    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
