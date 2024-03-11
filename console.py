import cmd
import shlex
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    '''AirBnb Command Processor'''

    intro = "CLI for AirBnB app"
    prompt = "Enter a comand:"
    
    def do_quit(self, line):
        '''Quit command to exit program '''
        return (True)

    def do_EOF(self, line):
        '''End of file'''
        return (True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
