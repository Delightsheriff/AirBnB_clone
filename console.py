#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """The HBNB console"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit the Console"""
        return True

    def do_EOF(self, line):
        """Ctrl + D"""
        print()
        return True

    def emptyline(self):
        """Empty Line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
