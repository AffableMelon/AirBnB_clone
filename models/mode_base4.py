import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    ''' Defines all common attributes and methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''
        Initializes a BaseModel instance
            *args not used
            **kwargs not empty, go thru keys (attr name)
                make sure it isn't __class__
                each value is the attr name
        '''

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        self.created_at = datetime.now()
                    elif key == 'updated_at':
                        self.updated_at = datetime.now()
                    else:
                        setattr(self, key, value)
                        storage.new(self)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = uuid.uuid4().hex
            storage.new(self)

    def __str__(self):
        """" Retruns a string of the BaseModel instance """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Update public instance update_at with the current save time """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a dictionary containg all key and values of self.__dict__"""

        copied_dict = self.__dict__.copy()
        copied_dict['__class__'] = self.__class__.__name__
        copied_dict['updated_at'] = self.updated_at.isoformat()
        copied_dict['created_at'] = self.created_at.isoformat()
        return(copied_dict)
