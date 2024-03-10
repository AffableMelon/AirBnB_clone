import json

class FileStorage:
    '''
    Serializes instances to JSON file.
    Deseializes JSON file to instances
    '''

    def __init__(self):
        self.__file_path = "file.json" # str to file path
        self.__objects = {} # store all objects by classname.id

    def all(self):
        ''' returns objects dict '''
        return(self.__objects)
    
    def new(self, obj):
        '''
        adds passed argument obj into __obejcts
        key obj's classname.id
        '''

        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        '''objects dict -> JSON'''
        ser_obj = {}
        for key, value in self.__objects.items():
            ser_obj[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(ser_obj, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    obj = globals().__class__.___name__
                    slef.__objects[key] = obj
        except FileNotFoundError:
            pass
