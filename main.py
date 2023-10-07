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
    if desired_function == "1": save_modset(input("Save New Modset as:"), modsets_directory, mc_mods_folder)
    if desired_function == "2": use_modset(input("What is the name of the modset you want to use? (Enter Name): "), modsets_directory, mc_mods_folder)
    if desired_function == "3": view_modsets()
    if desired_function == "4": check_modset(input("What is the name of the modset you would like to check? (enter the full name):"))
    if desired_function == "5": delete_modset(input("What modset would you like to delete?"), modsets_directory)
    if desired_function == "6": data_setup(False)
    if desired_function == "7": exit()

    start()


def save_modset(modset_name, modsets_directory, mc_mods_folder):
    
    os.mkdir(os.path.join(modsets_directory, modset_name))
    print("Modset folder created.")

    for mod in os.listdir(mc_mods_folder):
        mod = os.path.join(mc_mods_folder, mod)
        shutil.copy(mod, os.path.join(modsets_directory, modset_name))
        print("Copied mod from:"+str(mod))

    print("Modset Saved.")


def use_modset(modset_name, modsets_directory, mc_mods_folder):

    for mod in os.listdir(os.path.join(modsets_directory, modset_name)):

        mod = os.path.join(modsets_directory, modset_name, mod)
        shutil.copy(mod, mc_mods_folder)
        print("Modset Used.\n")


def delete_modset(modset_name, modsets_directory):
    shutil.rmtree(os.path.join(modsets_directory, modset_name))
    print("Modset Deleted\n")


def view_modsets():
    os.listdir(modsets_directory)


def check_modset(modset_name, modsets_directory):
    os.listdir(os.path.join(modsets_directory, modset_name))


data_check()
initialize()
start()