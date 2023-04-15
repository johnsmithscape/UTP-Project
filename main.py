###   ###  #######  ######### ##      #
#  ###  # #       #    ###    # #     #
#   #   # #########    ###    #  #    #
#       # #       #    ###    #    #  #
#       # #       # ######### #      ## useless .py file :D


# read_config(), create_config() in fuctions.py
# other (adb, fastboot, etc...) in helpers.py 

# read_config(), create_config() находятся в fuctions.py 
# другие (adb, fastboot, и т.д) находят в helpers.py
from fuctions import *
print("""


 ___  ___  _________  ________   
|\  \|\  \|\___   ___\\   __  \  
\ \  \\\  \|___ \  \_\ \  \|\  \ 
 \ \  \\\  \   \ \  \ \ \   ____\\
  \ \  \\\  \   \ \  \ \ \  \___|
   \ \_______\   \ \__\ \ \__\   
    \|_______|    \|__|  \|__|   v0.3 Recode season
                                 
/dev/Microtanki [Ivan], 4pda, https://4pda.to/forum/index.php?showuser=9457591""")

try:
    read_config()
except(ModuleNotFoundError, NameError, UnboundLocalError):
    create_config() 

