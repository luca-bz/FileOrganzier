import os
import shutil



class Organizer:
    def __init__(self):
        self.current_dir = r'F:\\Programmieren\\Python\\FileOrganzier'
        self.current_directory = os.getcwd()


    def organize(path):
        try:
            files = os.listdir(path)
            for file in files:
                filename, extentions = os.path.splitext(file)
                extentions = extentions[1:]
                print(extentions)
                move_from = path + "/" + file
                move_to = path + "/" + extentions + "/" + file
                c = path + "/" + extentions
                if os.path.exists(c):
                    shutil.move(move_from, move_to)
                else:
                    os.makedirs(c)
                    shutil.move(move_from, move_to)
        except PermissionError:
            print("You dont have permission")
                    

Organizer.organize(r'F:\\Programmieren\\Python\\FileOrganzier')