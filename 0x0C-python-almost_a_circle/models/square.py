#!/usr/bin/python3

'''
import the parent class Rectangle
'''

from rectangle import Rectangle

'''
create the child class Square that inherits from Rectangle
'''

class Square(Rectangle):
    '''
    create the public instance attribute size
    '''
    def __int__(self, size, x=0, y=0, id=None):
        '''
        calling the super class to assign attributes from the parent class
        '''
        super().__init__(
        size, size, x, y, id
        )
    
    @property
    def size(self):
        '''
        get the size of one side of the square
        '''
        return self.width
    
    @size.setter
    def size(self, value):
        '''
        set the size of the square
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        string representation of the class
        '''
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.size}'
    
    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''
        dictionary representation of the square
        '''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y':self.y}
