#!/usr/bin/python3
""" console.py that contains the entry point of the command interpreter
"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import models


class HBNBCommand(cmd.Cmd):
    """Simple command processor for airbnb."""
    prompt = '(hbnb) '
    class_dict = {"Amenity" : Amenity, "BaseModel": BaseModel, 
                  "City" : City, "Place" : Place, "Review" : Review,
                  "State" : State, "User" : User}

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("ctrl+D Quit command to exit the program\n")

    def emptyline(self):
        pass

    def do_create(self, line):
        if (line):
            if (line in self.class_dict):
                new_instance = self.class_dict[line]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        if(line):
            str_list = []
            str_list = line.split(" ")
            if (str_list[0] in self.class_dict):
                if(len(str_list) >= 2):
                    key = str_list[0]+"."+str_list[1]
                    show_dict = models.storage.all()
                    try:
                        print(show_dict[key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        if (line):
            str_list = []
            str_list = line.split(" ")
            if (str_list[0] in self.class_dict):
                if(len(str_list) >= 2):
                    key = str_list[0]+"."+str_list[1]
                    destro_dict = models.storage.all()
                    try:
                        destro_dict.pop(key)
                        models.storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        list_values = []
        all_dict = models.storage.all()
        if (line):
            if (line in self.class_dict):
                list_k = []
                for k, v in all_dict.items():
                    lista_k = k.split(".")
                    expresion = line + "." + lista_k[1]
                    if (expresion == k):
                        list_values.append(str(v))
                print(list_values)
                return
            else:
                print("** class doesn't exist **")
                return
        else:
            for v in all_dict.values():
                list_values.append(str(v))
            print(list_values)

    def do_update(self, line):
        if (line):
            str_list = []
            att_name = ""
            att_value = ""
            str_list = line.split(" ")
            if (str_list[0] in self.class_dict):
                if(len(str_list) >= 2):
                    key = str_list[0]+"."+str_list[1]
                    update_dict = models.storage.all()
                    if (len(str_list) >= 3):
                        att_name = str_list[2]
                        if (len(str_list) >= 4):
                            att_value = str_list[3]
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                    try:
                        match = False
                        for k, v in update_dict.items():
                            if (k == key):
                                v.__dict__.update({att_name: att_value[1:-1]})
                                models.storage.save()
                                match = True
                                break
                        if(match is False):
                            raise KeyError()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
