import os
import shutil
import pickle
import tkinter as tk


def setup():

    minecraft_directory = input("What is the path to your minecraft_directory? (C:/path/to/your/.minecraft):")

    if not os.path.exists(minecraft_directory): 
        next = input("ERROR: Invalid Path, make sure you have entered the correct path. Press ENTER to close")
        exit()

    terminal_or_gui = input("Would you like to use the terminal interface or the gui? (t/g)")

    if not terminal_or_gui == 'g' or not terminal_or_gui == 't': terminal_or_gui = 't'

    MM_Data_Dict = {

        'minecraft_directory': minecraft_directory,
        'terminal_or_gui': minecraft_directory
    }

    with open("MM_Data_Dict", "wb") as i: pickle.dump(MM_Data_Dict, i)
