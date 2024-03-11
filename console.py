#!/usr/bin/python3
import cmd
from shlex import split
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''AirBnb Command Processor'''

    intro = "CLI for AirBnB app"
    prompt = "(hbnb)"

    def emptyline(self):
        """Do nothing for no command pass"""
        pass

    def do_create(self,arg):
        """Usage: create <class>
        create a new class and print its id
        """
        argument_p = parse(arg)
        if len(argument_p):
            if argument_p[0] not in HBNBCommand.__classes:
                print ("** class doesn't exist **")
            else:
                print(eval(argument_p[0]).id)
                storage.save()

    def do_quit(self, line):
        '''Quit command to exit program '''
        return (True)

    def do_EOF(self, line):
        '''End of file'''
        print("")
        return (True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
