from time import sleep
from random import random


def add_3_names():
    my_file = open("names.txt", "a")
    for i in range(3):
        name = input("Enter name: ")
        my_file.write(name + "\n")
    my_file.close()

    return


def print_all_names():
    my_file = open("names.txt", "r")
    for name in my_file.readlines():
        print(f"Hello {name}")
    my_file.close()

    return


add_3_names()
print_all_names()
