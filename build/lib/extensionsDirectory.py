# Class containing all the File Extensions for the Package
class fileExtensions:

    """
    Stores all the File Extensions Supported by the Current Version.
    """

    # Constructor
    def __init__(self):

        # Defining the File Extensions
        self.picture_extensions = ['.jpeg', '.jpg', '.jpx', '.png', '.bnp', '.tiff', '.gif', '.raw', '.eps', '.bmp',
                                   '.nef', '.webp',
                                   '.cr2', '.tif', '.bmp', '.jxr', '.psd', '.ico', '.heic', '.svg']
        self.document_extensions = ['.txt', '.md', '.pdf', '.doc', '.odt', '.ods', '.docx', '.xls', '.xlsx', '.csv',
                                    '.tex', '.ppt',
                                    '.pptx', '.rtf', '.wpd', '.tsv', '.db']
        self.music_extensions = ['.mp3', '.mpeg', '.wav', '.wma', '.3gp', '.aac', '.wma', '.amr', '.flac', '.mid',
                                 '.m4a', '.ogg']
        self.video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.m4v', '.webm', '.wmv', '.mpg']
        self.archived_extensions = ['.epub', '.zip', '.tar', '.rar', '.gz', '.bz2', '.7z', '.xz', '.swf', '.rtf',
                                    '.eot', '.ps', '.sqlite', '.nes', '.crx', '.cab', '.deb', '.ar', '.Z', '.lz']
        self.programming_extensions = ['.cpp', '.cxx', '.py', '.c', '.java', '.js', '.jsx', '.css', '.html', '.go',
                                       '.h', '.m', '.php',
                                       '.pl', '.r', 'scala', '.jsp', '.asp', '.htm', '.cs', '.asmx', '.xhtml', '.aspx',
                                       '.ts', '.mm', '.cu',
                                       '.jav', '.j', '.jar', '.pl', '.pas', '.pyc', '.pyo', '.pyd', '.swift', '.yaws',
                                       '.rb', '.rhtml', '.rss',
                                       '.xml', '.json', '.ipynb', '.applescript', '.ino', '.asm', '.bat', '.cmd', '.bf',
                                       '.csx', '.clj',
                                       '.dockerfile', '.ex', '.exs', '.emacs', '.erl', '.graphql', '.dot', '.gz',
                                       '.jinja', '.jl', '.kt', '.ktm',
                                       '.kts', '.mak', '.mk', '.mkfile', '.matlab', '.pkl', '.pb', '.rs', '.sql',
                                       '.sci', '.vue', '.yml']

        # Defining the File Extensions into a Common Dictionary
        self.file_Extension_Group = dict()
        self.file_Extension_Group['Pictures'] = self.picture_extensions
        self.file_Extension_Group['Documents'] = self.document_extensions
        self.file_Extension_Group['Music'] = self.music_extensions
        self.file_Extension_Group['Videos'] = self.video_extensions
        self.file_Extension_Group['Archived'] = self.archived_extensions
        self.file_Extension_Group['Programming'] = self.programming_extensions

    # Method to get the Extensions according to its Type
    def getExtension(self, extension_type = None):

        if extension_type:
            return self.file_Extension_Group[extension_type]
        else:
            return self.file_Extension_Group



