import cmd
import shlex
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    '''AirBnb Command Processor'''

    intro = "CLI for AirBnB app"
    prompt = "Enter a comand:"

    def do_create(self, line):
        '''
        create a new instance of BaseModel
        save to json file
        print id
        '''
        class_name = line.shlex.split()[0]
        if not line:
            print("*** class name missing ***")
        elif class_name not in self.classes.keys():
            print (" *** class doesn't exist ***")
        



    def do_quit(self, line):
        '''Quit command to exit program '''
        return (True)

    def do_EOF(self, line):
        '''End of file'''
        return (True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
