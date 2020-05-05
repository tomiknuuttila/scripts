import datetime
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


now = datetime.datetime.now()


def checkForNotesFolder():
    notesFolder = os.environ['NOTES_FOLDER']
       if not notesFolder:
            print(
                f"{bcolors.WARNING}'Please setup enviroment variable NOTES_FOLDER{bcolors.ENDC}")
        else:
            print(
                f"{bcolors.OKGREEN}NOTES_FOLDER is defined as\n{bcolors.ENDC}", notesFolder)


print(f"{bcolors.OKGREEN}Current date is\n{bcolors.ENDC}", now.date())
os.chdir(notesFolder)
print(os.getcwd())
