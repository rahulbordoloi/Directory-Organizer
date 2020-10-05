from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name = 'directory_organizer',
    version = '1.0.5',
    description = 'Utility Package that organizes and moves the specific file types to its type Specific Directories',
    url = "https://github.com/rahulbordoloi/Directory-Organizer/",
    author = "Rahul Bordoloi",
    author_email = "rahulbordoloi24@gmail.com",
    maintainer = "Sourav Mazumdar",
    maintainer_email = "souravmzdr@gmail.com",

    py_modules = ['directory_organizer', 'oopsImplementation', 'extensionsDirectory'],
    package_dir = {'': 'src'},

    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop"
    ],

    long_description = long_description,
    long_description_content_type = "text/markdown",

    extras_require = {
        "dev" : [
            "pytest >= 3.7",
        ],
    },
)