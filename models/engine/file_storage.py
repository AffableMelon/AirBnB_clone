import json
from models.mode_base4 import BaseModel


class FileStorage:
    '''
    Serializes instances to JSON file.
    Deseializes JSON file to instances
    '''
    __file_path = "file.json"    # name of file to save into
    __objects = {}               # store all objects by classname.id

    def all(self):
        ''' returns objects dict '''
        return(FileStorage.__objects)

    def new(self, obj):
        '''
        adds passed argument obj into __obejcts
        key obj's classname.id
        '''

        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        '''objects dict -> JSON'''
        ser_obj = {}
        for key in FileStorage.__objects.keys():
            ser_obj[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(ser_obj, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
                for value in data.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
