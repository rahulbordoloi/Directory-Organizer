# Importing Class
from extensionsDirectory import fileExtensions

# Importing Libraries
import shutil
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join


# Class `Directory Organizer`
class directoryOrganizer:

    """
    Implementation Class of Package 'Directory Organizer.
    """

    # Constructor
    def __init__(self, path = None, verbose = False):

        # Checking Condition for Default Argument
        if not path:

            path = "Downloads"

            # Setting Home Directory Path
            self.homedir = str(Path.home())

            # Set the Source Directory Path [i.e the Downloads Path by DEFAULT]
            self.source = os.path.join(self.homedir, path)

        else:

            # Set the Source Directory Path [when Path isn't Downloads]
            self.source = os.path.join(path)

        # Copying All Files Names Present in the Source Directory
        self.all_files = [files for files in listdir(self.source) if isfile(join(self.source, files))]

        '''
        NOTE - We can change the "/Downloads" path to any other appropriate path if this script is required to run in 
        that Directory.
        '''

        # List Containing the files to be Moved
        self.documents = []
        self.pictures = []
        self.music = []
        self.videos = []
        self.archived = []
        self.programming = []
        self.others = []

        # Including All Types of File Extensions Possible

        ## Calling 'fileExtensions' class
        file_ext = fileExtensions()

        ## Adding file extensions in required places to include that files in that directory
        self.picture_ext = file_ext.getExtension('Pictures')
        self.document_ext = file_ext.getExtension('Documents')
        self.music_ext = file_ext.getExtension('Music')
        self.video_ext = file_ext.getExtension('Videos')
        self.archived_ext = file_ext.getExtension('Archived')
        self.programming_ext = file_ext.getExtension('Programming')

        ## Adding CAPS Extensions too
        self.picture_ext += [i.upper() for i in self.picture_ext]
        self.document_ext += [i.upper() for i in self.picture_ext]
        self.music_ext += [i.upper() for i in self.music_ext]
        self.video_ext += [i.upper() for i in self.video_ext]
        self.archived_ext += [i.upper() for i in self.archived_ext]
        self.programming_ext += [i.upper() for i in self.programming_ext]

        # Flag if the User wants to Print the Output into the Console [Files that are been moved & its Status]
        self.flag = verbose

        # Dictionary to Keep Track of the Files Moved according to their Type
        self.historyDictionary = {}

        # Extracting Information about the Files Present
        self.extractingFiles()

    # Method which extracts Information about the Files Present
    def extractingFiles(self):

        # Searching for Files and Categorising
        for files in self.all_files:

            if files.endswith(tuple(self.picture_ext)):
                self.pictures.append(files)
            elif files.endswith(tuple(self.document_ext)):
                self.documents.append(files)
            elif files.endswith(tuple(self.music_ext)):
                self.music.append(files)
            elif files.endswith(tuple(self.video_ext)):
                self.videos.append(files)
            elif files.endswith(tuple(self.archived_ext)):
                self.archived.append(files)
            elif files.endswith(tuple(self.programming_ext)):
                self.programming.append(files)
            else:
                self.others.append(files)

    # Display Method to Print Operation(s) [Show Moved Files] [Verbose]
    def printMovedFiles(self, datatype = 'Others'):

        # Initialising List of Files Items & Setting up their Type
        fileList = None

        if datatype == 'Documents':
            fileList = self.documents
        if datatype == 'Pictures':
            fileList = self.pictures
        if datatype == 'Music':
            fileList = self.music
        if datatype == 'Videos':
            fileList = self.videos
        if datatype == 'Archived':
            fileList = self.archived
        if datatype == 'Programming':
            fileList = self.programming
        elif datatype == 'Others':
            fileList = self.others

        # Prints the Output to the Console if `verbose` is True
        if self.flag:
            print(f'{len(fileList)} Files moved to {datatype}!')
            for file in fileList:
                print(file)

    # Method Handling the Moving Mechanism
    def moveFilesToDir(self, datatype = 'Others'):

        # Setting up Destination Directory according to Extension Type for Transfer
        destination = os.path.join(self.source, datatype)
        self.checkDirExists(destination)

        # File Move Initiation
        if datatype in ['Music', 'Archived', 'Programming']:
            print(f"Moving {datatype} File Extensions ...")
        else:
            print(f"Moving {datatype[:-1]} File Extensions ...")

        # Initialising List of Files Items & Setting up their Type
        fileList = None

        if datatype == 'Documents':
            fileList = self.documents
        elif datatype == 'Pictures':
            fileList = self.pictures
        elif datatype == 'Music':
            fileList = self.music
        elif datatype == 'Videos':
            fileList = self.videos
        elif datatype == 'Archived':
            fileList = self.archived
        elif datatype == 'Programming':
            fileList = self.programming
        elif datatype == 'Others':
            fileList = self.others

        # Moving the Files from Source to Destination
        for file in fileList:
            shutil.move(os.path.join(self.source, file), os.path.join(destination, file))

        # Print Moved Files into the Console if `verbose` is True
        if self.flag:
            self.printMovedFiles(datatype)

    # Method to Check if Required Files are Present [for Moving] and calling Appropriate Functions accordingly
    def checkCondition(self):

        ## Check for whether the files exists for a Particular Category type or Not

        if len(self.documents) != 0:
            self.moveFilesToDir('Documents')
        else:
            print("No Documents to Move!")

        if len(self.pictures) != 0:
            self.moveFilesToDir('Pictures')
        else:
            print("No Pictures to Move!")

        if len(self.music) != 0:
            self.moveFilesToDir('Music')
        else:
            print("No Music Files to Move!")

        if len(self.videos) != 0:
            self.moveFilesToDir('Videos')
        else:
            print("No Videos to Move!")

        if len(self.archived) != 0:
            self.moveFilesToDir('Archived')
        else:
            print("No Archived Files to Move!")

        if len(self.programming) != 0:
            self.moveFilesToDir('Programming')
        else:
            print("No Programming Files to Move!")

        if len(self.others) != 0:
            self.moveFilesToDir('Others')
        else:
            print("No Miscellaneous Files to Move!")

    # Method to check for Existence of a Directory [if it DNE, creates a New One]
    def checkDirExists(self, path):

        if not os.path.isdir(path):
            os.makedirs(path)

    # Method for Giving out the Dictionary of the Files Being Moved [History]
    def showHistory(self, extension_type = None):

        ## Putting Files lists up in a dictionary for Portability

        self.historyDictionary['Documents'] = self.documents
        self.historyDictionary['Pictures'] = self.pictures
        self.historyDictionary['Music'] = self.music
        self.historyDictionary['Videos'] = self.videos
        self.historyDictionary['Archived'] = self.archived
        self.historyDictionary['Programming'] = self.programming
        self.historyDictionary['Others'] = self.others

        if extension_type:
            return self.historyDictionary[extension_type]
        else:
            return self.historyDictionary







