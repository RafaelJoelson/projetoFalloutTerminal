import sys
import time

def robco_welcome_animation():
    robco_welcome = (
        "WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n"
    )

    for char in robco_welcome:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)


def robco_rit_animation():
    robco_welcome = (
        "RIT-V300\n"
    )

    for char in robco_welcome:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def robco_load1_animation():
    robco_welcome = (

        "Initializing Robco Industries(TM) MF Boot Agent v2.3.0\n"
        "RETRO BIOS\n"
        "RBIOS-4.02.08.00 52EE5.E7.E8\n"
        "Copyright 2201-2203 Robco Ind.\n"
        "Uppermen: 64KB"
        "Root (5A8)\n"
        "Maintenance Mode\n"
    )

    for char in robco_welcome:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)

def robco_login_animation():
    robco_welcome = (

        "WELCOME ADMINISTRATOR - PLEASE ENTER PASSWORD NOW:\n"
    )

    for char in robco_welcome:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)