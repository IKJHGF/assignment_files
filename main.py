__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# In main.py, write the following functions:

# 1. clean_cache: 
# takes no arguments and creates an empty folder named cache in the current directory. 
# If it already exists, it deletes everything in the cache folder.

# Danger
# This function deals with deleting files. 
# You should always be careful with this! 
# You should always do a dry run with print statements that to check 
# if everything is going according to plan before you commit to running the script. 
# We are not responsible if you mess up your system!

import os
import shutil

os.chdir("/Users/marschavandijk/Documents/Winc/files")

current_path = os.getcwd() 
dir_name = "cache"
path = os.path.join(current_path, dir_name)

def clean_cache():   
    if os.path.isdir("cache"):
        shutil.rmtree("cache")
    os.mkdir("cache")

clean_cache()
    
# 2. cache_zip: takes a zip file path (str) 
# and a cache dir path (str) as arguments, in that order. 
# The function then unpacks the indicated zip file into a clean cache folder.
# You can test this with data.zip file.

import zipfile
from zipfile import ZipFile

file = "cache.zip"

folder_cache = current_path + "/cache"
zip_file = current_path + "/data.zip"

def cache_zip(zip_file, folder_cache):
    with ZipFile(zip_file, "r") as zip:
        zip.extractall(folder_cache)
    return cache_zip

# 3. cached_files: takes no arguments and returns 
# a list of all the files in the cache. 
# The file paths should be specified in absolute terms. 
# Search the web for what this means! No folders should be included in the list. 
# You do not have to account for files within folders within the cache directory.

import pathlib

def cached_files():
    list_files = []
    with os.scandir(folder_cache) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                result = os.path.abspath(entry)
                list_files.append(result)
    return list_files

# 4. find_password: takes the list of file paths from cached_files as an argument. 
# This function should read the text in each one to see if the password is in there. 
# Surely there should be a word in there to indicate the presence of the password? 
# Once found, find_password should return this password string.

word = "password"
list_files = []

def find_password(list_files):
    for file in list_files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "password" in line:
                    password_in_line = line.split(" ")
                    return str(password_in_line[1]).strip()


if __name__ == "__main__":
    clean_cache()
    cache_zip("data.zip", "cache")
    cached_files()
    find_password(list_files)

print(find_password(cached_files()))