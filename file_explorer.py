#imports
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import subprocess, platform

#tkinter initialization and setup
t = Tk()
t.geometry("700x700")
t.title("File Explorer")

#opens file explorer to get root directory path
root_folder = filedialog.askdirectory()
print(root_folder)

#gets a list of all files and folders in root
files_and_folders = os.listdir()

#stores folders inside of root directory
folders = []

#stores item paths in root directory
item_paths = []

folder_item_paths = []

#displays all files inside root directory to a listbox
def browseRootFolder(root_folder):
    for item in os.listdir(root_folder):
        listbox.insert(tk.END, item)
    appendFolders(root_folder)

def appendFolders(folder):
    for item in os.listdir(folder):
        item_path = folder + "/" + item
        if os.path.isdir(item_path):
            folders.append(item_path)
            appendFolders(item_path)
    #for item in os.listdir(folder):
        #item_path = folder + "/" + item
        #if os.path.isdir(item_path):
           # folders.append(item_path)

#searches given root folder for file
def searchFolder(search_entry):
    listbox.delete(0, tk.END)
    appendFolders(root_folder)
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        item_paths.append(item_path)
        if search_entry in item.lower():
            listbox.insert(tk.END, item)
    for folder in folders:
        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            folder_item_paths.append(item_path)
            if search_entry in item.lower():
                listbox.insert(tk.END, item)

def openFile(file_path):
    if platform.system() == 'Darwin':
        subprocess.call(('open', file_path))
    elif platform.system() == 'Windows':
        os.startfile(file_path)
    else:
        subprocess.call(('xdg-open', file_path))

    
def openFileLocation(event):
    index = listbox.curselection()
    selected_index = index[0]
    selected_item = listbox.get(selected_index)
    print(selected_item)
    if os.path.basename(selected_item) in [os.path.basename(item_path) for item_path in item_paths]:
        item_name = listbox.get(index)
        item_path = os.path.join(root_folder, item_name)
        open(item_path)
    elif os.path.basename(selected_item) in [os.path.basename(folder_path) for folder_path in folder_item_paths]:
        folder_indices = [i for i, path in enumerate(folder_item_paths) if os.path.basename(path) == os.path.basename(selected_item)]
        item_name = listbox.get(index)
        selected_folder_index = folder_indices[0]
        item_path = folder_item_paths[selected_folder_index]
        openFile(item_path)
        
    else:
        print("File not found in either location!")
        
#tkinter widget setup
matching_items = []
searchbox = tk.Entry()
searchbox.pack()
searchbox_button = tk.Button(text = "Search", command=lambda: searchFolder(searchbox.get()))
searchbox_button.pack()
listbox = Listbox()
listbox.pack(fill=tk.BOTH, expand=True)
listbox.bind("<Button-1>", openFileLocation)


#runs tkinter and opens initial file browser for root directory
browseRootFolder(root_folder)
t.mainloop()


