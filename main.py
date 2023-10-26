import os
import shutil
import pickle
import tkinter as tk

version="v1.0.0"


def status_log(message):
    if terminal_or_gui == 't': print(message)
    if terminal_or_gui == 'g': gui_infotext.insert(tk.END, str("\n"+message))


def data_check():
    if os.path.isfile(os.path.join(os.getcwd(),"MM_data_dict")) == False:
        data_setup(False)


def data_setup(data_ready):

    if not data_ready:
        print("Starting ModManger"+version+" Config")
        modsets_directory = input("Where will your Modsets be kept? (enter 'n' to store it in the cwd, (reccomended)):")
        mc_mods_folder = input("What is the path to your mods folder? (Make sure to enter the entire path!): ")
        terminal_or_gui = input("Would you like to use terminal interface or gui? (t/g): ")

        if modsets_directory == "n":
            modsets_directory = "MM_Data"
            try: 
                os.mkdir(modsets_directory)
            except FileExistsError: 
                pass


        MM_data_dict= {
            'modsets_directory' : modsets_directory,
            'terminal_or_gui' : terminal_or_gui,
            'mc_mods_folder': mc_mods_folder,
        }

        with open("MM_data_dict", "wb") as i: pickle.dump(MM_data_dict, i)


def initialize_data():

    global MM_data_dict
    global modsets_directory
    global mc_mods_folder
    global terminal_or_gui

    with open("MM_data_dict", "rb") as i: MM_data_dict = pickle.load(i)

    modsets_directory = MM_data_dict['modsets_directory']
    terminal_or_gui = MM_data_dict['terminal_or_gui']
    mc_mods_folder = MM_data_dict['mc_mods_folder']


def initialize_window():

    global window
    global gui_infotext

    window = tk.Tk()
    window.title("ModManager " + version)

    #Functions are re-defined because command= param in tk.button doesn't work properly.
    def save_modset_local():
        save_modset(save_modset_name_entry.get(), modsets_directory, mc_mods_folder)

    def use_modset_local():
        use_modset(use_modset_name_entry.get(), modsets_directory, mc_mods_folder)

    def delete_modset_local():
        delete_modset(delete_modset_name_entry.get(), modsets_directory)

        
    save_modset_label = tk.Label(text="Enter the name of a modset you would like to save in box below and click button save it:")
    save_modset_name_entry = tk.Entry()
    save_modset_button = tk.Button(text="Save Modset:", command=save_modset_local)

    use_modset_label = tk.Label(text="Enter the name of a modset you would like to use in the box below:")
    use_modset_name_entry = tk.Entry()
    use_modset_button = tk.Button(text="Use Modset:", command=use_modset_local)

    delete_modset_label = tk.Label(text="Enter the name of a modset you would like to delete in the box below:")
    delete_modset_name_entry = tk.Entry()
    delete_modset_button = tk.Button(text="Delete Modset:", command=delete_modset_local)

    switch_to_terminal_button = tk.Button(text="Press to switch to terminal", command=switch_interface)

    gui_infotext = tk.Text(height=20, width=100)

    save_modset_label.pack()
    save_modset_name_entry.pack()
    save_modset_button.pack()

    use_modset_label.pack()
    use_modset_name_entry.pack()
    use_modset_button.pack()

    delete_modset_label.pack()
    delete_modset_name_entry.pack()
    delete_modset_button.pack()

    switch_to_terminal_button.pack()

    gui_infotext.pack()


def terminal_intro():

    print("ModManager v0.0.1, Developed By MSTF Studios\n")
    print("Chose an action from the prompts by typing its number and pressing enter.")
    print("1-Create a new modset")
    print("2-Use a saved modset")
    print("3-View saved modsets")
    print("4-Check the contents of a modset")
    print("5-Delete a saved modset")
    print("6-Switch to GUI (NEEDS RESTART)")
    print("7-Configure application settings")
    print("8-Exit ")

    desired_function = input (": ")

    #Checks what the user wants to do and then executes the respective function.
    if   desired_function == "1": save_modset(input("Save New Modset as:"), modsets_directory, mc_mods_folder)
    elif desired_function == "2": use_modset(input("What is the name of the modset you want to use? (Enter Name): "), modsets_directory, mc_mods_folder)
    elif desired_function == "3": view_modsets()
    elif desired_function == "4": check_modset(input("What is the name of the modset you would like to check? (enter the full name):"))
    elif desired_function == "5": delete_modset(input("What modset would you like to delete?"), modsets_directory)
    elif desired_function == "6": switch_interface()
    elif desired_function == "7": data_setup(False)
    elif desired_function == "8": exit()
    else: temporary = input("PlEASE ENTER A VALID INPUT, PRESS ENTER TO CONTINUE: ")

    terminal_intro()


def switch_interface():

    if MM_data_dict['terminal_or_gui'] == 'g': 
        MM_data_dict['terminal_or_gui'] = 't'
        with open("MM_data_dict", "wb") as i: pickle.dump(MM_data_dict, i)
        exit()

    if MM_data_dict['terminal_or_gui'] == 't': 
        MM_data_dict['terminal_or_gui'] = 'g'
        with open("MM_data_dict", "wb") as i: pickle.dump(MM_data_dict, i)
        exit() 


def save_modset(modset_name, modsets_directory, mc_mods_folder):

    try:  
        os.mkdir(os.path.join(modsets_directory, modset_name))
        status_log("Modset folder created.")

        for mod in os.listdir(mc_mods_folder):
            mod = os.path.join(mc_mods_folder, mod)
            shutil.copy(mod, os.path.join(modsets_directory, modset_name))
            status_log("Copied mod:"+str(mod))

        status_log("Modset Saved.")

    except FileNotFoundError:
        print("\nERROR: Your saved Mod directory is invalid, please reconfigure it.\n")
    

    except FileExistsError:
        status_log("\nERROR: A modset with that name already exists, please try again.")


def use_modset(modset_name, modsets_directory, mc_mods_folder):

    true_cwd = os.getcwd() #Change back to once all mods in mc_mods_folder are removed.

    os.chdir(mc_mods_folder)

    for mod in os.listdir():
        os.remove(mod)

    os.chdir(true_cwd)

    for mod in os.listdir(os.path.join(modsets_directory, modset_name)):

        mod = os.path.join(modsets_directory, modset_name, mod)
        shutil.copy(mod, mc_mods_folder)

    status_log("Modset Used.")


def delete_modset(modset_name, modsets_directory):
    if modset_name == "":
        status_log("You must use an existing modset.")
    else:
        shutil.rmtree(os.path.join(modsets_directory, modset_name))
        status_log("Modset Deleted")


def view_modsets():
    os.listdir(modsets_directory)


def check_modset(modset_name, modsets_directory):
    os.listdir(os.path.join(modsets_directory, modset_name))


data_check()
initialize_data()

if terminal_or_gui == "g":
    initialize_window()
    window.mainloop()

elif terminal_or_gui == "t":
    terminal_intro()

else:
    next = input("DELETE MM_DATA_DICT FROM LOCAL FOLDER AND RERUN PROGRAM. MAKE SURE TO SELECT g or t WHEN ASKED. PRESS ENTER TO CONTINUE:")
