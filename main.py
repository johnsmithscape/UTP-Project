import os

print('Добро пожаловать в UTP (Useful Tools Pack - Пак полезных инструментов)\n\n#      #  ########  ######\n#      #     ##     #     #\n#      #     ##     ######\n#      #     ##     #\n ######   ########  #\n\n(4pda.to, Vankinok, https://4pda.to/forum/index.php?showuser=9457591)')
tool = int(input('Список доступных инструментов\n1. Прошивка рекавери\n2. Прошивка firmware\n3. Зашив прошивки(для recovery)\n4. Магиск\nЧтобы продолжить - напишите цифру от 1 до 4 => '))
if tool == 1:
    
    print('Вы выбрали - "Прошивка рекавери"')
    print('Подключите ваше устройство в режиме fastboot')
    
    twrp = int(input('Список доступных кастомных рекавери\n1. twrp skkk a11\n2. twrp skkk a12\n3. twrp skkk a13\n4. orange fox recovery stable\n5. orange fox recovery beta\n6. свое рекавери (c именем recovery.img) => '))
   
    if twrp == 1:

        print('Загрузка twrp skkk a11')
        os.system("aria2c https://deac-fra.dl.sourceforge.net/project/recovery-for-xiaomi-devices/alioth/twrp-3.6.0_11-v3.1_A11-alioth-skkk.img")
        os.system("fastboot boot twrp-3.6.0_11-v3.1_A11-alioth-skkk.img")
        print('Чтобы установить тврп на постоянку:\n1. Переходил раздел advanced (допольнительные настойки)\n2. Жмем на flash current twrp (прошить текущий тврп)')
        input('Готово (нажмите enter для выхода)')
        exit(0)
    
    elif twrp == 2:

        print('Загрузка twrp skkk a12')
        os.system("aria2c https://deac-fra.dl.sourceforge.net/project/recovery-for-xiaomi-devices/alioth/twrp-3.7.0_12-v7.0_A12-alioth-skkk.img")
        os.system("fastboot boot twrp-3.7.0_12-v7.0_A12-alioth-skkk.img")
        print('Чтобы установить тврп на постоянку:\n1. Переходил раздел advanced (допольнительные настойки)\n2. Жмем на flash current twrp (прошить текущий тврп)')
        input('Готово (нажмите enter для выхода)')
        exit(0)

    elif twrp == 3:
        
        print('Загрузка twrp skkk a13')
        os.system("aria2c https://deac-fra.dl.sourceforge.net/project/recovery-for-xiaomi-devices/alioth/twrp-3.7.0_12-v7.0_A13-alioth-skkk.img")
        os.system("fastboot boot twrp-3.7.0_12-v7.0_A13-alioth-skkk.img")
        print('Чтобы установить тврп на постоянку:\n1. Переходил раздел advanced (допольнительные настойки)\n2. Жмем на flash current twrp (прошить текущий тврп)')
        input('Готово (нажмите enter для выхода)')
        exit(0)
         
    elif twrp == 4:
        
        print('Загрузка orange fox recovery stable')
        os.system("aria2c https://us-dl.orangefox.download/63315c533c05f43c193c13b6")
        os.system("7za x OrangeFox-alioth-stable@R11.1_1_A12.zip recovery.img")
        os.system("fastboot boot recovery.img")
        print('Чтобы установить orange fox recovery на постоянку:\n1. Заходим в меню (3 горизонтальные полоски)\n2. Листаем вниз и жмем на Flash current OrangeFox(прошить текущий OrangeFox)')
        input('Готово (нажмите enter для выхода)')
        exit(0)
    
    elif twrp == 5:
        
        print('Загрузка orange fox recovery beta')
        os.system("aria2c https://us-dl.orangefox.download/6308b4793c05f43c193bed5b")
        os.system("7za x OrangeFox-alioth-beta@R11.1_1_5_A12.zip recovery.img")
        os.system("fastboot boot recovery.img")
        print('Чтобы установить orange fox recovery на постоянку:\n1. Заходим в меню (3 горизонтальные полоски)\n2. Листаем вниз и жмем на Flash current OrangeFox(прошить текущий OrangeFox)')
        input('Готово (нажмите enter для выхода)')
        exit(0)
    
    elif twrp == 6:
        
        print('Свое рекавери (c именем recovery.img)')
        input('Переименуйте образ рекавери в recovery.img и нажмите enter')
        os.system("fastboot boot recovery.img")
        print('Чтобы установить тврп на постоянку:\n1. Переходил раздел advanced (допольнительные настойки)\n2. Жмем на flash current twrp (прошить текущий тврп)\n\nЧтобы установить orange fox recovery на постоянку:\n1. Заходим в меню (3 горизонтальные полоски)\n2. Листаем вниз и жмем на Flash current OrangeFox(прошить текущий OrangeFox)')
        input('Готово (нажмите enter для выхода)')
        exit(0)
    
    else:
        
        exit(0)

elif tool == 2:
    fw = int(input('1. EU 13.0.9.0\n2. Global (MI) 13.0.6.0\n3. Свой firmware (с именем fw.zip) => '))
    
    if fw == 1:
        
        print("Вы выбрали - EU 13.0.9.0")
        print("Перейдите в режим рекавери и запустите adb sideload")
        os.system("aria2c https://bot.siddrive.ga/0:/fw_alioth_miui_ALIOTHEEAGlobal_V13.0.9.0.SKHEUXM_f9603cf7f3_12.0.zip")
        os.system("adb wait-for-device")
        os.system("adb sideload fw_alioth_miui_ALIOTHEEAGlobal_V13.0.9.0.SKHEUXM_f9603cf7f3_12.0.zip")
        input("Готово (нажмите enter для выхода)")
        exit(0)
    
    elif fw == 2:

        print("Вы выбрали - Global (MI) 13.0.6.0")
        print("Перейдите в режим рекавери и запустите adb sideload")
        os.system("aria2c https://void.siddrive.ga/0:/fw_alioth_miui_ALIOTHGlobal_V13.0.6.0.SKHMIXM_e83b44e411_12.0.zip")
        os.system("adb wait-for-device")
        os.system("adb sideload fw_alioth_miui_ALIOTHGlobal_V13.0.6.0.SKHMIXM_e83b44e411_12.0.zip")
        input("Готово (нажмите enter для выхода)")
        exit(0)
   
    elif fw == 3:
        
        print("Поместите ваш firmware с именем fw.zip")
        input("Чтобы продолжить нажмите enter")
        print("Перейдите в режим рекавери и запустите adb sideload")
        os.system("adb wait-for-device")
        os.system("adb sideload fw.zip")
        input("Готово (нажмите enter для выхода)")
        exit(0)
    
    else:
        
        exit(0)

elif tool == 3:
   
    print('Вы выбрали - "Зашив прошивки (для recovery)"')
    print("Переименуйте файл прошивки в rom.zip")
    input("Чтобы продолжить нажмите enter")
    print("Перейдите в режим рекавери и запустите adb sideload")
    os.system("adb wait-for-device")
    os.system("adb sideload rom.zip")
    input("Готово (нажмите enter для выхода)")
    exit(0)

elif tool == 4:
    
    print('Вы выбрали - "Магиск"')
    mgsk = int(input("1. - Magisk Stable v25.2 \n2. - Magisk Canary\n3. - Magisk Debug\n4. - Свой магиск => "))
    
    if mgsk == 1:

        print('Magisk Stable v25.2')
        os.system("aria2c https://github.com/topjohnwu/Magisk/releases/download/v25.2/Magisk-v25.2.apk")
        print("Перейдите в режим рекавери и запустите adb sideload")
        os.system("mv Magisk-v25.2.apk Magisk-v25.2.zip")
        input("Чтобы продолжить нажмите enter")
        os.system("adb wait-for-device")
        os.system("adb sideload Magisk-v25.2.zip")
        input("Готово (нажмите enter для выхода)")
        exit(0)

    elif mgsk == 2:

        print('Magisk Canary')
        os.system("aria2c https://raw.githubusercontent.com/topjohnwu/magisk-files/canary/app-release.apk")
        print("Перейдите в режим рекавери и запустите adb sideload")
        os.system("mv app-release.apk Magisk-Canary.zip")
        input("Чтобы продолжить нажмите enter")
        os.system("adb wait-for-device")
        os.system("adb sideload Magisk-Canary.zip")
        input("Готово (нажмите enter для выхода)")
        exit(0)

    elif mgsk == 3:

        print('Magisk Debug')
        os.system("aria2c https://raw.githubusercontent.com/topjohnwu/magisk-files/canary/app-debug.apk")
        print("Перейдите в режим рекавери и запустите adb sideload")
        os.system("mv app-debug.apk Magisk-Debug.zip")
        input("Чтобы продолжить нажмите enter")
        os.system("adb wait-for-device")
        os.system("adb sideload Magisk-Debug.zip")
        input("Готово (нажмите enter для выхода)")
        exit(0)

    elif mgsk == 4:

        print("Поместите Magisk с именем magisk.zip")
        print("Перейдите в режим рекавери и запустите adb sideload")
        input("Чтобы продолжить нажмите enter")
        os.system("adb wait-for-device")
        os.system("adb sideload magisk.zip")
        input("Готово (нажмите enter для выхода)")
        exit(0)

    else:

        exit(0)

else:
    
    exit(0)       
    

        

