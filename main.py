import os
import shutil
import pickle

version="v0.0.1"

def data_check():
    if os.path.isfile("MM_data_dict") == False:
        data_setup(False)


def data_setup(data_ready):

    if data_ready == False:
        print("Starting ModManger"+version+" Config")
        modsets_directory=input("Where do you want to store ModManager Modsets? Make sure to enter a full path. (or enter 'n' to store it where this script is located, this is reccomended):")
        mc_mods_folder=input("What is the path to your mods folder? (eg. C:/Users/me/AppData/Roaming/.minecraft/mods) (Make sure to enter the entire path!)")

        if modsets_directory == "n": 
            modsets_directory = "MM_Data"
            try: 
                os.mkdir(modsets_directory)
            except FileExistsError: 
                pass

        MM_data_dict= {
            'modsets_directory' : modsets_directory,
            'mc_mods_folder': mc_mods_folder
        }

        with open("MM_data_dict", "wb") as i: pickle.dump(MM_data_dict, i)


def initialize():
    pass

def start():
    pass

def save_modset(modset_name, modsets_directory, mc_mods_folder):
    pass

def use_modset(modset_name, modsets_directory, mc_mods_folder):
    pass

def delete_modset(modset_name, modsets,_directory):
    pass

data_check()
initialize()