import os
import shutil
import tkinter as tk
from tkinter import filedialog as fd

class Organizer:

    """
    def gui():
        root = tk.Tk()
        root.title('Select Folder')
        root.resizable(False, False)
        root.geometry('350x150')



        def select_folder():
            folder = fd.askdirectory(
                title='Select directory')
            Organizer.organize(folder)

        def quit():
            exit()

        open_btn = tk.Button(root, text='Select a Folder', command=select_folder)
        quit_btn = tk.Button(root, text='Quit', command=quit)
        open_btn.pack(expand=True)
        quit_btn.pack(expand=True)
        # run the application
        root.mainloop()
    """

    def organize(path):

            try:
                files = os.listdir(path)
                for file in files:
                    filename, extentions = os.path.splitext(file)
                    extentions = extentions[1:]
                    move_from = path + "/" + file
                    move_to = path + "/" + extentions + "/" + file
                    c = path + "/" + extentions
                    if os.path.exists(c):
                        shutil.move(move_from, move_to)
                    else:
                        os.makedirs(c)
                        shutil.move(move_from, move_to)
            except PermissionError:
                print()
                print("You dont have permission")
                    

if __name__ == "__main__":
    Organizer.organize(os.getcwd())