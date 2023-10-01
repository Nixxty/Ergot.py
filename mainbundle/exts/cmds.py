from os import system, name
from time import sleep

### ascii art bcuz its pretty :3
## indexes | 0 = bot splash | 1 = DATACHOV splash | 2 = SELECTOR splash | 3 = nothing
asciisplashes = ["\n\n▓█████  ██▀███    ▄████  ▒█████  ▄▄▄█████▓\n▓█   ▀ ▓██ ▒ ██▒ ██▒ ▀█▒▒██▒  ██▒▓  ██▒ ▓▒\n▒███   ▓██ ░▄█ ▒▒██░▄▄▄░▒██░  ██▒▒ ▓██░ ▒░\n▒▓█  ▄ ▒██▀▀█▄  ░▓█  ██▓▒██   ██░░ ▓██▓ ░ \n░▒████▒░██▓ ▒██▒░▒▓███▀▒░ ████▓▒░  ▒██▒ ░ \n░░ ▒░ ░░ ▒▓ ░▒▓░ ░▒   ▒ ░ ▒░▒░▒░   ▒ ░░   \n ░ ░  ░  ░▒ ░ ▒░  ░   ░   ░ ▒ ▒░     ░    \n   ░     ░░   ░ ░ ░   ░ ░ ░ ░ ▒    ░      \n   ░  ░   ░           ░     ░ ░           \n\n", "\n\n                     ▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄                              \n                     ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄                            \n                     ░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄                          \n                     ░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██                         \n                     ░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒                        \n                      ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░                        \n                      ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░                        \n                      ░ ░  ░   ░   ▒    ░        ░   ▒                           \n                        ░          ░  ░              ░  ░                        \n                      ░                                                          \n             ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███               \n            ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒             \n            ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒             \n            ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄               \n            ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒             \n            ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░             \n              ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░             \n            ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░              \n            ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░                  \n            ░                       ░                                            \n ▒█████   ██▒   █▓▓█████  ██▀███   █     █░ ██▀███   ██▓▄▄▄█████▓▓█████  ██▀███  \n▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓█░ █ ░█░▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒\n▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒▒█░ █ ░█ ▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒\n▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░█░ █ ░█ ▒██▀▀█▄  ░██░░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  \n░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒░░██▒██▓ ░██▓ ▒██▒░██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒\n░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▓░▒ ▒  ░ ▒▓ ░▒▓░░▓    ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░\n  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░  ▒ ░ ░    ░▒ ░ ▒░ ▒ ░    ░     ░ ░  ░  ░▒ ░ ▒░\n░ ░ ░ ▒       ░░     ░     ░░   ░   ░   ░    ░░   ░  ▒ ░  ░         ░     ░░   ░ \n    ░ ░        ░     ░  ░   ░         ░       ░      ░              ░  ░   ░     \n              ░                                                                  \n\n", "\n\n ██░ ██  ▄▄▄       ███▄    █ ▓█████▄  ██▓    ▓█████  ██▀███  \n▓██░ ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌▓██▒    ▓█   ▀ ▓██ ▒ ██▒\n▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░    ▒███   ▓██ ░▄█ ▒\n░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██░    ▒▓█  ▄ ▒██▀▀█▄  \n░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░██████▒░▒████▒░██▓ ▒██▒\n ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░\n ░  ░░ ░  ░   ▒      ░   ░ ░  ░ ░  ░   ░ ░      ░     ░░   ░ \n ░  ░  ░      ░  ░         ░    ░        ░  ░   ░  ░   ░     \n                              ░                              \n\n", '']

# clear function to clear the terminal for prettiness
def clearterminal(sleeptime, ascii):
    sleep(int(sleeptime))
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')
    print(asciisplashes[int(ascii)])

