#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
import shlex
import sys
import re
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    all_classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ function to exit the cmd """
        return True

    def do_EOF(self, line):
        """ function to exit the cmd """
        print()
        return True

    def help_quit(self):
        """ help guide for quit command """
        print('Quit command to exit the program')

    def help_EOF(self):
        """ help guide for EOF command """
        print('EOF command to exit the program')

    def emptyline(self):
        """ handles empty lines """
        pass

    def do_help(self, line):
        """overrides help method"""
        cmd.Cmd.do_help(self, line)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            cls = globals()[class_name]
            new_inst = cls()
            print(new_inst.id)
            storage.save()

    # Other methods (do_show, do_destroy, do_all, do_update, do_count, default)
    # ...

if __name__ == "__main__":
    HBNBCommand().cmdloop()
