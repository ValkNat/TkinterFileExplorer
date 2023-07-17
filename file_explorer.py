#imports
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import subprocess

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
    print(folders)
    for item in os.listdir(root_folder):
        if search_entry in item.lower():
            listbox.insert(tk.END, item)
    for folder in folders:
        for item in os.listdir(folder):
            if search_entry in item.lower():
                listbox.insert(tk.END, item)
    
def openFileLocation(event):
    index = listbox.curselection()
    if index:
        directory = os.path.dirname()
        
#tkinter widget setup
matching_items = []
searchbox = tk.Entry()
searchbox.pack()
searchbox.bind("<Button-1>", openFileLocation)
searchbox_button = tk.Button(text = "Search", command=lambda: searchFolder(searchbox.get()))
searchbox_button.pack()
listbox = Listbox()
listbox.pack(fill=tk.BOTH, expand=True)

#runs tkinter and opens initial file browser for root directory
browseRootFolder(root_folder)
t.mainloop()


