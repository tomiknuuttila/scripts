import datetime
import os
from pathlib import Path
from shutil import copyfile


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def goToNotesFolderRoot():
    notesFolder = os.environ['NOTES_FOLDER']

    if notesFolder:
        os.chdir(notesFolder)
    else:
        exit()
    os.chdir(notesFolder)


def moveToFolder(folder):
    if not Path(folder).exists():
        print(f"{bcolors.OKGREEN}Creating a new folder: \n{bcolors.ENDC}", folder)
        os.makedirs(folder)
    os.chdir(folder)


def generateFilename(dateArray):
    dateArray.reverse()
    filename = "".join(str(x) for x in dateArray) + ".tex"
    return filename


def getPathToPreviousEntry(current):
    goToNotesFolderRoot()
    previous = current - datetime.timedelta(1)
    folders = str(previous).split('-')
    filename = generateFilename(folders.copy())

    for folder in folders:
        moveToFolder(folder)

    if not os.path.isfile(filename):
        getPathToPreviousEntry(previous)

    return str(os.path.abspath(filename))

def getPathToCurrentDate(current):
    goToNotesFolderRoot()
    folders = str(date).split('-')
    filename = generateFilename(folders.copy())
    for folder in folders:
        moveToFolder(folder)

    return os.getcwd() + "/" + filename



now = datetime.datetime.now()
date = now.date()

pathToPreviousEntry = getPathToPreviousEntry(date)
pathToCurrentDate = getPathToCurrentDate(date)

if not os.path.isfile(pathToCurrentDate):
    print(f"{bcolors.OKGREEN}Copying from previous entry: \n{bcolors.ENDC}", pathToPreviousEntry)
    copyfile(pathToPreviousEntry, pathToCurrentDate)
    print(f"{bcolors.OKGREEN}Created entry for today: \n{bcolors.ENDC}", pathToCurrentDate)
else:
    print(f"{bcolors.OKGREEN}File already exists: \n{bcolors.ENDC}", pathToCurrentDate)


