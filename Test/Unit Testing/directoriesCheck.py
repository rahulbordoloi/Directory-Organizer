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

        ## NOTE - We can change the "/Downloads" path to any other appropriate path if this script is required to run in that Directory

        # List Containing the files to be Moved
        self.documents = []
        self.pictures = []
        self.musics = []
        self.videos = []
        self.archived = []
        self.programming = []
        self.others = []

        # Including All Types of File Extensions Possible

        ## Calling 'fileExtensions' class
        file_ext = fileExtensions()

        ## Adding file extensions in required places to include that files in that directory
        self.picture_ext = file_ext.getExtension('picture_ext')
        self.document_ext = file_ext.getExtension('document_ext')
        self.music_ext = file_ext.getExtension('music_ext')
        self.video_ext = file_ext.getExtension('video_ext')
        self.archived_ext = file_ext.getExtension('archived_ext')
        self.programming_ext = file_ext.getExtension('programming_ext')

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
                self.musics.append(files)
            elif files.endswith(tuple(self.video_ext)):
                self.videos.append(files)
            elif files.endswith(tuple(self.archived_ext)):
                self.archived.append(files)
            elif files.endswith(tuple(self.programming_ext)):
                self.programming.append(files)
            else:
                self.others.append(files)

    # Unit Tester Method
    def unitTesterExtensions(self):

        print(f"Pictures : {len(self.pictures)}")
        print(f"Documents : {len(self.documents)}")
        print(f"Music : {len(self.musics)}")
        print(f"Videos : {len(self.videos)}")
        print(f"Archived : {len(self.archived)}")
        print(f"Programming : {len(self.programming)}")
        print(f"Others : {len(self.others)}")
        print(f"Programming : {self.programming}")
        print(f"Others : {self.others}")


# Main Method
if __name__ == '__main__':
    obj = directoryOrganizer()
    obj.unitTesterExtensions()
