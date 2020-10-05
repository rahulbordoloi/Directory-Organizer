# Importing Class
from oopsImplementation import directoryOrganizer
from extensionsDirectory import fileExtensions

# Importing Libraries
import time


# Package Class
class organizer:

    """
    Directory Organizer is a simple open-sourced python package that scans one's folder directory and moves the specific
    file types to its type-specific directories.
    """

    # Constructor
    def __init__(self, path = None, verbose = False):

        # Initialising Class Variables

        self.path = path
        self.verbose = verbose
        self.moveFilesObject = None          # Class Object

        # Using Error Handling Techniques to Handle Error(s)

        try:
            start = time.time()
            self.moveFilesObject = directoryOrganizer(self.path, self.verbose)
            self.moveFilesObject.checkCondition()
            end = time.time()
            print('Time Elapsed : ', round(end - start, 2), 'seconds')

        except Exception as exception:

            print("Please Try Again! An Unexpected Error has Occurred!")
            print(f"Type : {type(exception)}")
            print(f"Error : {exception}")

    # Method to Get Moved Files History
    def showHistory(self, extension_type = None):

        return self.moveFilesObject.showHistory(extension_type)

    # Method to Show Version Number
    @property
    def __version__(self) -> str:

        return '1.0.5'

    # Method to Display File Extensions Supported Currently
    def showExtensions(self, extension_type = None):

        if extension_type:
            return fileExtensions().getExtension(extension_type)
        else:
            return fileExtensions().getExtension()





