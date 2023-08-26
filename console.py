#!/usr/bin/python3
""" The HBNB console """
import cmd
import shlex
import sys
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The HBNB console"""

    prompt = "(hbnb) "
    all_classes = {
        "BaseModel",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review",
        "User"
    }

    list_of_models = ["BaseModel", "User", "State",
                      "Review", "City", "Amenity", "Place"]


    def do_help(self, line):
        """overrides help method"""
        cmd.Cmd.do_help(self, line)

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, line):
        """ function to exit the cmd """
        return True

    def emptyline(self):
        """ handles empty lines """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a Class, saves it (to the JSON file), and prints its id.
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return

        cls = globals()[class_name]
        if cls is None:
            print("** clase doesn't exist **")
            return

        new_inst = cls()
        # Save the instance to the JSON file
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        cls = globals().get(class_name)  # Get the class by name
        id = args[1]

        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return


        instances_dict = storage.all()  # get stored objects as dict
        id_list = []
        for key in instances_dict:
            class_name, inst_id = key.split(".")
            id_list.append(inst_id)

        if id in id_list:
            key = "{}.{}".format(class_name, id)
            instance = instances_dict[key]

            print(instance.__str__())
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
           print("** instance id missing ***")
           return

        key = "{}.{}".format(args[0], args[1])
        instances_dict = storage.all()  # get stored objects as dict
        if key not in instances_dict:
            print("** no instance found **")
        else:
            del instances_dict[key]
            storage.save()
    def do_all(self, arg):
       """
       Prints all string representations of instances based on the class name.
       If no class name is provided, prints all instances.
       """
       args = arg.split()
       obj_list = []

       inst_dict = storage.all()

       # Check if a valid class name is provided
       if len(args) > 0 and args[0] not in HBNBCommand.all_classes:
           print("** class doesn't exist **")
           return

       # Loop through instances and filter based on class name
       for key in inst_dict:
           inst = inst_dict[key]

           # Check if the class matches the provided class name
           if len(args) == 0 or (len(args) > 0 and args[0] == inst.__class__.__name__):
               obj_list.append(inst_dict[key].__str__())

       # Print the list of string representations
       print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
         and id by adding or updating attributes
        """
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing ")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attr = args[2]
        value = args[3]

        objects_dict = storage.all()

        # Construct the key based on class name and instance ID
        key = "{}.{}".format(class_name, instance_id)

        if key not in objects_dict:
            print("** no instance found **")
            return

        # Check if the attribute is one of the non-updatable attributes
        if attr in ["id", "created_at", "updated_at"]:
            print("This attribute cannot be updated.")
            return

        obj = objects_dict[key]
        setattr(obj, attr, value)
        storage.save()

    def do_count(self, arg):
        """ count instances """
        count = 0
        class_name = arg
        all_instances = storage.all()
        for key, obj in all_instances.items():
            name = key.split(".")
            if name[0] == class_name:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
