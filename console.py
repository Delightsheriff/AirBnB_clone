# Import the cmd module
import cmd


# Define a class that inherits from cmd.Cmd
class HBNBCommand(cmd.Cmd):
    # Set the prompt attribute to "(hbnb) "
    prompt = "(hbnb) "

    # Define a method called do_quit that takes self and arg as parameters
    def do_quit(self, arg):
        """Quit command to exit the program"""
        # Return True to indicate the end of the interpreter loop
        return True

    # Define a method called do_EOF that takes self and arg as parameters
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        # Print a new line
        print()
        # Return True to indicate the end of the interpreter loop
        return True

    # Define a method called emptyline that takes self as a parameter
    def emptyline(self):
        """Do nothing on empty input line"""
        # Pass
        pass


# Check if the module is executed as the main program
if __name__ == '__main__':
    # Create an instance of HBNBCommand and call the cmdloop method
    HBNBCommand().cmdloop()
