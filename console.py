#!/usr/bin/python3
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """EOF command to exit the program."""
        print()
        return True

    def help_help(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Called when empty line is entered in prompt."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
