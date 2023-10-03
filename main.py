import os
import shutil
import pickle
import glob

def Introduction(): #Starts and runs the program.

    global permadir
    permadir=os.getcwd()
    os.chdir(permadir)

    #Make pickles directory to store pickle files. WILL BE REMOVED LATER WHEN INSTALLER IS MADE
    if os.path.exists("pickles") == False: os.mkdir("pickles")

    #Loads mod directory path to modfolder variable from pickles/modfolder.pickle
    if os.path.exists("pickles/modfolder.pickle"):
        with open('pickles/modfolder.pickle', 'rb') as f:
            global modfolder
            modfolder = pickle.load(f) 

    #Interface text
    print("ModManager v0.0.1, Developed By MSTF Studios\n")
    print("Chose an action from the prompts by typing a number and pressing enter.")
    print("1-Create a new modset")
    print("2-Use a saved modset")
    print("3-View saved modsets")
    print("4-Delete a saved modset")
    print("5-Change or set mods folder")

    desired_function = input (": ")

    #Checks what the user wants to do and then executes the respective function.
    if desired_function == "1": save_modset()
    if desired_function == "2": use_modset()
    if desired_function == "3": view_modsets()
    if desired_function == "4": delete_modset()
    if desired_function == "5": mod_folder_config()


def save_modset(): #Creates a new modset from current mods folder and copies all the mods to a local folder
 if input("This will copy all mods in your mods folder to saved directory, do you want to proceed? (y/n): ") == "y":

    if os.path.exists("modsets") == False: os.mkdir("modsets")
    else: os.chdir("modsets")

    modset_name = input("What would you like this modset to be called? (Type desired name and press enter): ")

    os.mkdir(modset_name)
    premodlist = os.listdir(modfolder)

    for mod in premodlist:
        modpath = (os.path.join(modfolder, mod))
        shutil.copy(modpath, modset_name)


def use_modset():
    if input("This will DELETE ALL MODS CURRENTLY BEING USED and replace them with a modset, do you want to proceed? (y/n): ") == "y":
        #Deletes all mods in use.
        os.chdir(modfolder)
        for mod in os.listdir():
            os.chmod(mod, 0o777) 
            os.remove(mod)

        modset_tobe_used = input("What is the exact name of the modset you want to use? (Enter exact name): ")

        #Copies the modset to the mod folder.
        os.chdir(os.path.join(permadir ,"modsets"))
        shutil.copytree(os.path.join(permadir ,"modsets", modset_tobe_used), modfolder, dirs_exist_ok=True)

        print("Modset Used.")


def view_modsets():
    pass

def delete_modset():
    pass

def mod_folder_config(): #Changes or sets mod directory
    check_if_sure = input("Do you want to chnage or set a mod folder? (y/n): ")

    if check_if_sure == "y":
        modfolder = input("Input the full path to your mod folder: ")
        with open("pickles/modfolder.pickle", "wb") as f: pickle.dump(modfolder, f) 

            
Introduction() #This calls the Introduction function to start the program.