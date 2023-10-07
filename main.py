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
    with open("MM_data_dict", "rb") as i: MM_data_dict = pickle.load(i)

    global modsets_directory
    global mc_mods_folder

    modsets_directory = MM_data_dict['modsets_directory']
    mc_mods_folder = MM_data_dict['mc_mods_folder']

def start():

    print("ModManager v0.0.1, Developed By MSTF Studios\n")
    print("Chose an action from the prompts by typing a number and pressing enter.")
    print("1-Create a new modset")
    print("2-Use a saved modset")
    print("3-View saved modsets")
    print("4-Check the contents of a modset")
    print("5-Delete a saved modset")
    print("6-Configure application settings")
    print("7-Exit ")

    desired_function = input (": ")

    #Checks what the user wants to do and then executes the respective function.
    if desired_function == "1": save_modset()
    if desired_function == "2": use_modset()
    if desired_function == "3": view_modsets()
    if desired_function == "4": check_modset()
    if desired_function == "5": delete_modset()
    if desired_function == "6": data_setup(False)
    if desired_function == "7": exit()

    start()

def save_modset(modset_name, modsets_directory, mc_mods_folder):
    pass

def use_modset(modset_name, modsets_directory, mc_mods_folder):
    pass

def delete_modset(modset_name, modsets,_directory):
    pass

def view_modsets():
    pass

def check_modset():
    pass

data_check()
initialize()
start()