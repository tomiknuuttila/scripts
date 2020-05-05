import datetime
import os
from pathlib import Path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def checkForNotesFolder(notesFolder):
    if not notesFolder:
        return False
    else:
        return True


def moveToFolder(folder):
    if not Path(folder).exists():
        print(f"{bcolors.OKGREEN}Creating a new folder: \n{bcolors.ENDC}", folder)
        os.makedirs(folder)
    os.chdir(folder)


now = datetime.datetime.now()
notesFolder = os.environ['NOTES_FOLDER']

if checkForNotesFolder(notesFolder):
    os.chdir(notesFolder)
else:
    exit()

folders = str(now.date()).split('-')

for folder in folders:
    moveToFolder(folder)
print(os.getcwd())
