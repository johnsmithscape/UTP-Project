import os
from config import *
print('Добро пожаловать в UTP (Useful Tools Pack - Пак полезных инструментов)\n\n#      #  ########  ######\n#      #     ##     #     #\n#      #     ##     ######\n#      #     ##     #\n ######   ########  #\n\n(4pda.to, Vankinok, https://4pda.to/forum/index.php?showuser=9457591)')
tool = int(input('1. config builder\n2. config.py\nЧтобы продолжить - напишите цифру 1 или 2 => '))
if tool == 1:

    cfg_work = int(input("Какой инструмент вам нужен?\n1. прошивка recovery\n2. прошивка firmware\n3. зашив прошивки (recovery)\n4. magisk => "))
    cfg_name = "config.txt"
    if cfg_work == 1:
        cfg_tool = ('work_type = "recovery"')
        os.system("echo " + cfg_tool + " > " + cfg_name)
        cfg_rec = int(input("Какой тип рекавери вам нужен? (1. twrp, 2. ofox) => "))
        
        if cfg_rec == 1:
            
            twrp_type = ('recovery_type = "twrp"')
            os.system("echo " + twrp_type + " >> " + cfg_name)
            cfg_rec_path = input("Укажите полный путь до образа рекавери (Например /home/tux/recovery.img) : ")
            twrp_path = ('recovery_path = "' + cfg_rec_path + '"')
            os.system("echo " + twrp_path + " >> " + cfg_name)
            cfg_rec_guide = input("Хотите ли вы, чтобы программа рассказала вам о том, как установить рекавери на постоянку (true/false) => ")
            guide = ('show_guide = "' + cfg_rec_guide + '"')
            os.system("echo " + guide + " >> " + cfg_name)
            os.system('move /Y ' + cfg_name + ' config.py')
            input("\nГотово (нажмите enter для выхода)")
            exit(0)
        
        elif cfg_rec == 2:
            
            ofox_type = ('recovery_type = "ofox"')
            os.system("echo " + ofox_type + " >> " + cfg_name)
            cfg_rec_path = input("Укажите полный путь до установочного zip архива ofox (Например /home/tux/ofox.zip) : ")
            ofox_path = ('recovery_path = "' + cfg_rec_path + '"')
            os.system("echo " + ofox_path + " >> " + cfg_name)
            cfg_rec_unpack = input("Укажите каталог, который будет создан для распаковки архива ofox (Например /home/tux/utp/ofox) : ")
            ofox_unpack = ('unpackfolder = "' + cfg_rec_unpack + '"')
            os.system("echo " + ofox_unpack + " >> " + cfg_name)
            cfg_rec_guide = input("Хотите ли вы, чтобы программа рассказала вам о том, как установить рекавери на постоянку (true/false) => ")
            guide = ('show_guide = "' + cfg_rec_guide + '"')
            os.system("echo " + guide + " >> " + cfg_name)
            os.system('move /Y ' + cfg_name + ' config.py')
            input("\nГотово (нажмите enter для выхода)")
            exit(0)
        else:
            exit(0)

    elif cfg_work == 2:
        
        cfg_tool = ('work_type = "firmware"')
        os.system("echo " + cfg_tool + " > " + cfg_name)
        cfg_fw_path = input("Укажите расположение вашего firmware (Например /home/tux/fw.zip) : ")
        firmw_path = ('fw_path = "' + cfg_fw_path + '"')
        os.system("echo " + firmw_path + " >> " + cfg_name)
        os.system('move /Y ' + cfg_name + ' config.py')
        input("\nГотово (нажмите enter для выхода)")
        exit(0)
    
    elif cfg_work == 3:
        
        cfg_tool = ('work_type = "rom_recovery"')
        os.system("echo " + cfg_tool + " > " + cfg_name)
        cfg_rom_rec_path = input("Укажите расположение вашей прошивки (Например /home/tux/rom.zip) : ")
        rom_rec_path = ('rom_path = "' + cfg_rom_rec_path + '"')
        os.system("echo " + rom_rec_path + " >> " + cfg_name)
        os.system('move /Y ' + cfg_name + ' config.py')
        input("\nГотово (нажмите enter для выхода)")
        exit(0)
    
    elif cfg_work == 4:

        cfg_tool = ('work_type = "magisk"')
        os.system("echo " + cfg_tool + " > " + cfg_name)
        cfg_mgsk_file = input("Укажите источник магиска (my/download) : ")
        
        if cfg_mgsk_file == "my":

            mgsk_file = ('magisk_file = "' + cfg_mgsk_file + '"')
            os.system("echo " + mgsk_file + " >> " + cfg_name)
            cfg_mgsk_path = input("Укажите расположение магиска (Например /home/tux/magisk.zip: ")
            mgsk_path = ('magisk_path = "' + cfg_mgsk_path + '"')
            os.system("echo " + mgsk_path + " >> " + cfg_name)
            os.system('move /Y ' + cfg_name + ' config.py')
            input("\nГотово (нажмите enter для выхода)")
            exit(0)
        
        elif cfg_mgsk_file == "download":
            
            mgsk_file = ('magisk_file = "' + cfg_mgsk_file + '"')
            os.system("echo " + mgsk_file + " >> " + cfg_name)
            cfg_mgsk_ver = input("Укажите версию магиска (stable/canary/debug) : ")
            mgsk_ver = ('magisk_ver = "' + cfg_mgsk_ver + '"')
            os.system("echo " + mgsk_ver + " >> " + cfg_name)
            os.system('move /Y ' + cfg_name + ' config.py')
            input("\nГотово (нажмите enter для выхода)")
            exit(0)
        
        else:
            
            exit(0)
    
    else:
        print("Ошибка")
        exit(0)

elif tool == 2:
    print("Выбран config.py")
    if work_type == "recovery" and recovery_type == "twrp" and show_guide == "true":
        
        input("Перейдите в режим fastboot и нажмите enter")
        print("\nрасположение рекавери -", recovery_path, "\nтип рекавери -", recovery_type, "\nпоказывать гайд по прошивке рекавери после установки - ", show_guide, "\n")
        input("Убедитесь, что все правильно и нажмите enter")
        os.system("fastboot boot", recovery_path)
        print('Чтобы установить тврп на постоянку:\n1. Переходил раздел advanced (допольнительные настойки)\n2. Жмем на flash current twrp (прошить текущий тврп)')
        input("\nГотово (нажмите enter для выхода)")
        exit(0)

    elif work_type == "recovery" and recovery_type == "twrp" and show_guide == "false":
        
        input("Перейдите в режим fastboot и нажмите enter")
        print("\nрасположение рекавери -", recovery_path, "\nтип рекавери -", recovery_type, "\nпоказывать гайд по прошивке рекавери после установки - ", show_guide, "\n")
        input("Убедитесь, что все правильно и нажмите enter")
        os.system("fastboot boot", recovery_path)
        input("\nГотово (нажмите enter для выхода)")
        exit(0)
            
    elif work_type == "recovery" and recovery_type == "ofox" and show_guide == "true":

        print("\nрасположение рекавери -", recovery_path, "\nтип рекавери -", recovery_type, "\nпоказывать гайд по прошивке рекавери после установки -", show_guide, "\nпапка для распаковки -", unpackfolder, "\n")
        input("Убедитесь, что все правильно и нажмите enter")
        os.system('7za x ' + recovery_path + ' recovery.img && fastboot boot recovery.img')        
        print('Чтобы установить orange fox recovery на постоянку:\n1. Заходим в меню (3 горизонтальные полоски)\n2. Листаем вниз и жмем на Flash current OrangeFox(прошить текущий OrangeFox)')
        input("\nГотово (нажмите enter для выхода)")
        exit(0) 
    
    elif work_type == "recovery" and recovery_type == "ofox" and show_guide == "false":

        print("\nрасположение рекавери -", recovery_path, "\nтип рекавери -", recovery_type, "\nпоказывать гайд по прошивке рекавери после установки -", show_guide, "\nпапка для распаковки -", unpackfolder, "\n")
        input("Убедитесь, что все правильно и нажмите enter")
        os.system('7za x ' + recovery_path + ' recovery.img && fastboot boot recovery.img')
        input("\nГотово (нажмите enter для выхода)")
        exit(0)

    elif work_type == "firmware":
        
        print("\nрасположение firmware -", fw_path, "\n")
        input("Убедитесь, что все правильно и нажмите enter\n")
        input("Перейдите в режим рекавери и запустите adb sideload и нажмите enter")
        os.system("adb sideload " + fw_path)
        input("\nГотово (нажмите enter для выхода)")
        exit(0)
    
    elif work_type == "rom_recovery":
        
        print("\nрасположение прошивки (recovery) -", rom_path, "\n")
        input("Убедитесь, что все правильно и нажмите enter\n")
        input("Перейдите в режим рекавери и запустите adb sideload и нажмите enter")
        os.system("adb sideload " + rom_path)
        input("\nГотово (нажмите enter для выхода)")
        exit(0)
    
    elif work_type == "magisk" and magisk_file == "my":
            
        print("\nисточник магиска -", magisk_file, "\nрасположение магиска -", magisk_path, "\n")
        input("Убедитесь, что все правильно и нажмите enter\n")
        input("Перейдите в режим рекавери и запустите adb sideload и нажмите enter")
        os.system("adb sideload " + magisk_path)
        
    elif work_type == "magisk" and magisk_file == "download" and magisk_ver == "stable":
            
        print("\nисточник магиска -", magisk_file, "\nверсия магиска -", magisk_ver, "\n")
        input("Убедитесь, что все правильно и нажмите enter\n")
        input("Перейдите в режим рекавери и запустите adb sideload и нажмите enter")
        os.system("aria2c https://github.com/topjohnwu/Magisk/releases/download/v25.2/Magisk-v25.2.apk " + "&& mv Magisk-v25.2.apk Magisk-v25.2.zip && adb sideload Magisk-v25.2.zip")
        input("\nГотово (нажмите enter cfg_toolдля выхода)")
        exit(0)
    
    elif work_type == "magisk" and magisk_file == "download" and magisk_ver == "canary":
            
        print("\nисточник магиска -", magisk_file, "\nверсия магиска -", magisk_ver, "\n")
        input("Убедитесь, что все правильно и нажмите enter\n")
        input("Перейдите в режим рекавери и запустите adb sideload и нажмите enter")
        os.system("aria2c https://raw.githubusercontent.com/topjohnwu/magisk-files/canary/app-release.apk " + "&& mv app-release.apk Magisk-Canary.zip && adb sideload Magisk-Canary.zip")
        input("\nГотово (нажмите enter для выхода)")
        exit(0)
    
    elif work_type == "magisk" and magisk_file == "download" and magisk_ver == "debug":
            
        print("\nисточник магиска -", magisk_file, "\nверсия магиска -", magisk_ver, "\n")
        input("Убедитесь, что все правильно и нажмите enter\n")
        input("Перейдите в режим рекавери и запустите adb sideload и нажмите enter")
        os.system("aria2c https://raw.githubusercontent.com/topjohnwu/magisk-files/canary/app-debug.apk " + "&& mv app-debug.apk Magisk-Debug.zip && adb sideload Magisk-Debug.zip")
        input("\nГотово (нажмите enter для выхода)")
        exit(0)
        
    else:
            
        input("Ошибка! Проверьте файл config.py")
        exit(0)  

else:
    
    exit(0)