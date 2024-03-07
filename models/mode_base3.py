import uuid
from datetime import datetime


class BaseModel:
    ''' Defines all common attributes and methods for other classes'''

    def __init__(self):
        """ Initializes a BaseModel instance """

        self.created_at = datetime.now()   # setting creation datetime
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())         # set id and convert to string

    def __str__(self):
        """" Retruns a string of the BaseModel instance """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Update public instance update_at with the current save time """

        self.updated_at = datetime.now()

    def to_dict(self):
        """creates a dictionary containg all key and values of self.__dict__"""

        copied_dict = self.__dict__.copy()
        copied_dict['__class__'] = self.__class__.__name__
        copied_dict['updated_at'] = self.updated_at.isoformat()
        copied_dict['created_at'] = self.created_at.isoformat()
        return(copied_dict)
