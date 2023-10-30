import os
import shutil
import pickle
import tkinter as tk


def log(message):
    if terminal_or_gui == 't': print(message)
    if terminal_or_gui == 'g': print(message)

def setup():

    minecraft_directory = input("What is the path to your minecraft directory? (C:/path/to/your/.minecraft):")

    if not os.path.exists(minecraft_directory): 
        next = input("ERROR: Invalid Path, make sure you have entered the correct path. Press ENTER to close")
        exit()

    terminal_or_gui = input("Would you like to use the terminal interface or the gui? (t/g)")

    if not terminal_or_gui == 'g' or not terminal_or_gui == 't': terminal_or_gui = 't'

    MM_Data_Dict = {

        'minecraft_directory': minecraft_directory,
        'terminal_or_gui': terminal_or_gui
    }

    with open("MM_Data_Dict", "wb") as i: pickle.dump(MM_Data_Dict, i)
    print("Data Saved Sucsessfully!")

    try: os.mkdir("modsets")
    except FileExistsError: pass

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
    print("2-Use a saved modset")
    print("3-Check the contents of a modset")
    print("4-Delete a savded modset")
    print("5-Switch to GUI")
    print("6-Reconfigure settings")
    print("8-Exit")

    action = input(": ")
    
    if   action == "1":save_modset(input("New Modset Name:"), minecraft_directory)
    elif action == "2":use_modset(input("Which modset do you want to use:"), minecraft_directory)
    elif action == "8":exit()

    terminal_interface()

def save_modset(modset_name, minecraft_directory):
    true_cwd = os.getcwd()

    os.mkdir(os.path.join("modsets",modset_name))
    os.mkdir(os.path.join("modsets",modset_name,"mods"))
    os.mkdir(os.path.join("modsets",modset_name,"resourcepacks"))

    os.chdir(os.path.join(minecraft_directory, "mods"))

    for mod in os.listdir():
        shutil.copy(mod, os.path.join(true_cwd, "modsets", modset_name, "mods"))
        log("Sucsessfully copied mod:" + mod)

    os.chdir(os.path.join(minecraft_directory, "resourcepacks"))

    for pack in os.listdir():
        shutil.copy(pack, os.path.join(true_cwd, "modsets", modset_name, "resourcepacks"))
        log("Sucsessfully copied resourcepack:" + pack)
    
    log("Copied all mods and resourcepacks sucsessfully!")

    os.chdir(true_cwd)

def use_modset(modset_name, minecraft_directory):
    true_cwd = os.getcwd()

    os.chdir(os.path.join(minecraft_directory, "mods"))
    for mod in os.listdir():os.remove(mod)

    os.chdir(os.path.join(minecraft_directory, "resourcepacks"))
    for pack in os.listdir():os.remove(pack)
    
    os.chdir(true_cwd)
    os.chdir(os.path.join("modsets", modset_name, "mods"))

    for mod in os.listdir():
        shutil.copy(mod, os.path.join(minecraft_directory, "mods"))
        log(str("Imported Mod:" + mod))
    
    os.chdir(true_cwd)
    os.chdir(os.path.join("modsets", modset_name, "resourcepacks"))

    for pack in os.listdir():
        shutil.copy(pack, os.path.join(minecraft_directory, "resourcepacks"))
        log(str("Imported Resourcepack:" + pack))
    
    log("\nModset imported, you can now play!")

    os.chdir(true_cwd)


if not os.path.exists("MM_Data_Dict"): 
    setup()


load_data()
terminal_interface()
