# UTP-Project (windows branch)
U.T.P - Useful Tools Pack for POCO F3 (alioth)
# System requirements (Windows)
- Windows 7 and up
- aria2c (https://aria2.github.io/)
- 7zip (console version, windows, https://www.7-zip.org/download.html)
- platform tools (https://developer.android.com/studio/releases/platform-tools)
# Build requirements
- Python 3.8, pip
- PyInstaller `pip install PyInstaller`
# Build
`pyInstaller -i utp_logo.ico -F main.py`
have a fun! :D
# For 4PDA
### Как собрать свой config.py?
`work_type = "recovery"` # доступно: recovery / firmware / rom_recovery / magisk

#### Для прошивки recovery (work_type = "recovery"):
`recovery_type = "twrp"` # доступно: twrp / ofox

`recovery_path = "/home/tux/recovery.img"` # необходимо ввести путь до recovery.img (если он в папке с программой, то 
просто имя файла + его расширение, если recovery_type = "ofox", то указываем путь до zip архива ofox)

`show_guide = "true"` # доступно true / false (да / нет)

#### Для прошивки firmware (work_type = "firmware"):
`fw_path = "/home/tux/fw.zip"` # необходимо ввести путь до firmware (если он в папке с программой, то просто имя файла + его расширение)

#### Для зашива прошивки через recovery (work_type = "rom_recovery"):
`rom_path = "/home/tux/rom.zip"` # необходимо ввести путь до прошивки (если она в папке с программой, то просто имя файла + его расширение)

#### для прошивки магиска (work_type = "magisk"):
`magisk_file = "my"` # доступно: my (то есть ваш .zip архив) / download (то есть программа скачает магиск сама)

`magisk_path = "/home/tux/magisk.zip"` # необходимо ввести путь до magisk (если он в папке с программой, то просто 
имя файла + его расширение и только если magisk_file = "my")

`magisk_ver = "stable"` # stable / canary / debug (только если magisk_file = "download")
