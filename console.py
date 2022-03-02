#!/usr/bin/python3
""" console.py that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """Simple command processor for airbnb."""
    prompt = '(hbnb) '
    
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
            if (line == "BaseModel"):
                new_instance = BaseModel()
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
            if (str_list[0] == "BaseModel"):
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
            if (str_list[0] == "BaseModel"):
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
            if (line == "BaseModel"):
                for v in all_dict.values():
                    list_values.append(str(v))
                print(list_values)
            else:
                print("** class doesn't exist **")
        else:
            for v in all_dict.values():
                list_values.append(str(v))
            print(list_values)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    