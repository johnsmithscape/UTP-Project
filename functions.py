import os
import time
from helpers import *        
def create_config():
    print("Конфиг не найден, необходимо собрать его\n")
    print("""Какой инструмент вам нужен?
    1. прошивка recovery
    2. прошивка firmware
    3. зашив прошивки (recovery)
    4. magisk""")
    var = input(">> ")
    if var == '1': # recovery
        create_file("config.py")
        edit_file("config.py", 'work_type = \\"recovery\\"')
        recovery_path = input("Укажите полный путь до рекавери >> ")
        edit_file("config.py", f'img_path = \\"{recovery_path}\\"')
    elif var == '2': # firmware (abl, sbl, xbl, etc..)
        cfg_helper("firmware")
    elif var == '3': # rom (flashable zip for custom recovery)
        cfg_helper("rom_for_recovery")
    elif var == '4': # magisk
        cfg_helper("magisk")
    elif var == 'read_config()':
        read_config()
    exit(0)

def read_config():
    from config import work_type
    if work_type == "recovery":
        from config import img_path
        mode_switcher("bootloader")
        os.system("clear")
        fastboot("boot", img_path)
    elif work_type == "firmware" or work_type == "rom_for_recovery" or "magisk":
        from config import zip_path
        zip_flasher(zip_path)
    exit(0)