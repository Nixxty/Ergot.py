# Ergot.py
A discord bot focused on remote control of the host PC

IMPORTANT: Ensure that you set your data (Guild ID, Channel ID, Bot Token) properly, or else the bot will NOT work (safety precaution to prevent other users from controlling your PC)

NOTE: main.py handles EVERYTHING in this project. it runs the bot file and it checks for updates, etc. There is no need to run the Python files separately.

Source info:
Data format: JSON
Used Languages|
Python
Used Modules|
JSON
os
discord
gputil
psutil
datetime
random
string
subprocess

as of version 0.1-alpha-2, the bot can currently:
Take screenshots and send them to a channel.
Check your CPU usage, RAM usage, and GPU temps and neatly embed them into a channel.
shutoff your PC from Discord

version 0.1-alpha-2 update included:
Checks for channel ID, guild ID, and author ID, making the bot more secure.
a function that checks for updates by comparing the local version file on a PC to the GitHub version.
made everything run from main.py
