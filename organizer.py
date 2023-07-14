import os
import shutil
import tkinter as tk
from tkinter import filedialog as fd

class Organizer:

    def __init__(self, path):
         self.path = path

    def organize(self):

            try:
                files = os.listdir(self.path)
                for file in files:
                    filename, extentions = os.path.splitext(file)
                    extentions = extentions[1:]
                    move_from = self.path + "/" + file
                    move_to = self.path + "/" + extentions + "/" + file
                    c = self.path + "/" + extentions
                    if os.path.exists(c):
                        shutil.move(move_from, move_to)
                    else:
                        os.makedirs(c)
                        shutil.move(move_from, move_to)
            except PermissionError:
                print("You dont have permission")

f = os.getcwd()

Organizer(f)