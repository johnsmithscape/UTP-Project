# UTP-Project (linux branch)
U.T.P - Useful Tools Pack for POCO F3 (alioth)
# Run requirements
## Archlinux (Manjaro, Garuda, Arco, Artix, etc... (so, pacman based))
#### aria2 `pacman -S aria2`
#### android-tools `pacman -S android-tools`
#### unzip `pacman -S unzip`
## Ubuntu/Debian (apt based)
#### aria2 `apt install aria2`
#### android-tools `apt install adb fastboot`
#### unzip `apt install unzip`
## Gentoo/Calculate linux (portage based)
#### aria2 `emerge aria2`
#### android-tools `emerge android-tools`
#### unzip `emerge unzip`
# Build requirements
- Python3, pip
- PyInstaller `pip install PyInstaller`
# Build
`pyInstaller -i utp_logo.ico -F main.py`
have a fun! :D
