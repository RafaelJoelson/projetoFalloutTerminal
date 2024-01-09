from terminal_animations import robco_welcome_animation, robco_load1_animation, robco_rit_animation, robco_login_animation
from miniGameHacking import minigame_hacking
from robcoLogin import getpass_windows, verify_credentials
import getpass
command = ""
help_command = ""
set_terminal_command = "SET TERMINAL/INQUIRE"
set_file_command = "SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F"
set_halt_restart_command = "SET HALT RESTART/MAINT"
run_debug = "RUN DEBUG/ACCOUNTS.F"
robco_welcome_animation()
robco_login_animation()
senha = getpass_windows()
verify_credentials()
command = input(">").upper()
while not (command==set_terminal_command):
    print("Invalid command. Try again or type 'help'")
    command = input(">").upper()
robco_rit_animation()
command = input(">").upper()
while not (command==set_file_command):
    print("Invalid command. Try again or type 'help'")
    command = input(">").upper()
command = input(">").upper()
while not (command==set_halt_restart_command):
    print("Invalid command. Try again or type 'help'")
    command = input(">").upper()
robco_load1_animation()
command = input(">").upper()
while not (command==run_debug):
    print("Invalid command. Try again or type 'help'")
    command = input(">").upper()
robco_welcome_animation()
minigame_hacking()
