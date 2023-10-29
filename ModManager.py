import os
import shutil
import pickle
import tkinter as tk


def log(message):
    if terminal_or_gui == 'g': print(message)
    if terminal_or_gui == 't': print(message)

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
    print("Data Saved Sucsessfully!")


def load_data():
    global minecraft_directory
    global terminal_or_gui

    with open("MM_Data_Dict", "rb") as i: MM_Data_Dict = pickle.load(i)
    minecraft_directory = MM_Data_Dict['minecraft_directory']
    terminal_or_gui = MM_Data_Dict['terminal_or_gui']

def terminal_interface():
    print("\nModManager v1.1.0")
    print("Type the number of the respective action and press enter:")
    print("1-Create a new modset")

    action = input(": ")
