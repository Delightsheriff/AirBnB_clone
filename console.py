#!/usr/bin/python3
import cmd
from models import *


class HBNBCommand(cmd.Cmd):
    """The HBNB console"""
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates an instance of MyClass and prints its id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in valid_classes:
            """
            Checks if the class name exists in the
            valid_classes dictionary.
            """
        try:
            inst = valid_classes[args[0]]()
            storage.save()
            """Saves the instance to the storage dictionary."""
        except Exception as e:
            print(inst.id)
        else:
            print("** class doesn't exist **")
            """Prints an error message if the class name does not exist."""

    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            """Tries to get the instance from the storage dictionary."""
            obj = storage.all()[args[0] + "." + args[1]]
            print(obj)
        except KeyError:
            """Prints an error message if the instance does not exist."""
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in valid_classes:
            print("** class doesn't exist **")
        else:
            try:
                """
                Tries to get the key of the instance
                from the storage dictionary.
                """
                key = args[0] + "." + args[1]
                store = storage.all()[key]
                if key in storage.all().keys():
                    del storage.all()[key]
                    storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all instances of a class."""
        args = line.split()
        store = storage.all()
        x = store.values()
        if len(args) == 0:
            """Prints all instances in the storage dictionary."""
            objs = store.values()
        elif args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        else:
            """Prints all instances of the specified class."""
            objs = [obj for obj in x if type(obj).__name__ == args[0]]
            print([str(obj) for obj in objs])

    def do_update(self, line):
        """Updates an attribute of an instance."""
        args = line.split()
        store = storage.all()
        key = args[0] + "." + args[1]
        obj = store[key]
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        if key not in store:
            print("** no instance found **")

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr = args[2]
        value = args[3]

        if attr in ["id", "created_at", "updated_at"]:
            print("This attribute cannot be updated.")
            return

        value = eval(value)

        setattr(obj, attr, value)
        obj.save()

    def do_help(self, arg):
        """
        Display help information about the available commands.
        Usage: help [command]
        """
        if arg:
            # Show help for a specific command
            if arg == "quit":
                print("Quit command to exit the program\n")
            else:
                print("No help available for command:", arg)
        else:
            # Show a list of available commands
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help   quit\n")

    def do_quit(self, line):
        """Quit command to exit the program
        
        """
        return True

    def do_EOF(self, line):
        """Ctrl + D"""
        print()
        return True

    def emptyline(self):
        """ Do nothing """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
