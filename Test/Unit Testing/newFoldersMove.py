# Importing Dependencies
from src.directory_organizer import organizer
from src.oopsImplementation import directoryOrganizer


# Main Method
def main():

    obj = directoryOrganizer(move_folders = True)
    obj.checkCondition()
    # print(obj.showHistory('Folders'))
    # print(obj.__version__)


# Driver Method
if __name__ == '__main__':
    main()
