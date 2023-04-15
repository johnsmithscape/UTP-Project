import os
import time
def create_file(fullname):
    os.system(f"echo > {fullname}")
def edit_file(fullname, text):
    try:
        open(fullname)
    except:
        os.system(f'echo {text} > {fullname}')
    else:
        os.system(f'echo {text} >> {fullname}')
def delete_file(fullname):
    os.system(f"rm -rf {fullname}")
def rename_file(oldname, newname):
    os.system(f"mv {oldname} {newname}")

def adb(cmd, stuff = None, place = None):
    if cmd == "reboot":
        return os.system(f"adb reboot {stuff}")
    elif cmd == "wait":
        return os.system("adb wait-for-device")
    elif cmd == "sideload":
        return os.system(f"adb sideload {stuff}")
    elif cmd == "push":
        return os.system(f"adb push {stuff} {place}")
    elif cmd == "shell":
        return os.system(f"adb shell {stuff}")
    else:
        print("error")

def fastboot(cmd, stuff = None, place = None):
    if cmd == "boot":
        return os.system(f"fastboot boot {stuff}")
    elif cmd == "reboot":
        return os.system(f"fastboot reboot {stuff}")
    # other soon
    else:
        print("error")

def cfg_helper(var):
    create_file("config.py")
    edit_file(f"config.py", 'work_type = \\"{var}\\"')
    temp_path = input("Укажите полный путь до zip архива >> ")
    edit_file("config.py", f'zip_path = \\"{temp_path}\\"')

def zip_flasher(zip_path):
    adb("shell", "twrp sideload")
    time.sleep(1)
    adb("sideload", zip_path)



