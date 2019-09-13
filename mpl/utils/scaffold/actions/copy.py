import shutil
from distutils.dir_util import copy_tree

def copy_file(destination_path, file_path):
    shutil.copy(file_path, destination_path)

def copy_folder(destination_path, folder_path):
    copy_tree(folder_path, destination_path)
