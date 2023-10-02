import os
import shutil
import pickle

def Introduction():

    if os.path.exists("pickles") == False: os.mkdir("pickles")

    if os.path.exists("pickles/modfolder.pickle"):
        with open('pickles/modfolder.pickle', 'rb') as f:
            global modfolder
            modfolder = pickle.load(f) 

    print("ModManager v0.0.1, Developed By MSTF Studios\n")
    print("Chose an action from the prompts by typing a number and pressing enter.")
    print("1-Create a new modset")
    print("2-Use a saved modset")
    print("3-View saved modsets")
    print("4-Delete a saved modset")
    print("5-Change or set mods folder")

    desired_function = input (": ")

    if desired_function == "1": save_modset()
    if desired_function == "2": use_modset()
    if desired_function == "3": view_modsets()
    if desired_function == "4": delete_modset()
    if desired_function == "5": mod_folder_config()


def save_modset():

    if os.path.exists("modsets") == False: os.mkdir("modsets")
    else: os.chdir("modsets")

    modset_name = input("What would you like this modset to be called? (Type desired name and press enter): ")
    os.chdir("modsets/")
    os.mkdir(modset_name)
    premodlist = os.listdir(modfolder)

    for mod in premodlist:
        modpath = (os.path.join(modfolder, mod))
        shutil.copy(modpath, modset_name)


def use_modset():
    pass

def view_modsets():
    pass

def delete_modset():
    pass

def mod_folder_config():
    permission = input("Do you want to chnage or set a mod folder? (y/n): ")

    if permission == "y":
        modfolder = input("Input the full path to your mod folder: ")
        with open("pickles/modfolder.pickle", "wb") as f: pickle.dump(modfolder, f) 

            
Introduction()