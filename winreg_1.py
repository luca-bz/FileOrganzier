import os
import sys
import shutil
import winreg as r

    # windows registry: Computer\HKEY_CLASSES_ROOT\Folder\shellex\ContextMenuHandlers
    # https://www.online-tech-tips.com/computer-tips/windows-right-click-context-menu/
    # https://www.thewindowsclub.com/remove-click-context-menu-items-editors
    # https://stackoverflow.com/questions/8570288/run-python-script-on-selected-file
    # https://www.youtube.com/watch?v=jS2LuG1p8Vw&t=1s


def reg():
    cwd = os.getcwd() + '\\' + 'organizer.exe'

    key_path = r"Directory\\Background\\shell\\Organizer"

    # outer key
    key = r.CreateKeyEx(r.HKEY_CLASSES_ROOT, key_path)
    r.SetValue(key, '', r.REG_SZ, 'Organize folder')
    try:
        pkg = os.path.expanduser('~') + '\\' + 'organizer'
        os.mkdir(pkg)
        shutil.move(cwd, pkg)
    except:
        pass

    #inner key 
    key1 = r.CreateKeyEx(key, r"command")
    r.SetValue(key1, '', r.REG_SZ, r'C:\Users\Luca\organizer\organizer.exe')


if __name__ == '__main__':
    reg()