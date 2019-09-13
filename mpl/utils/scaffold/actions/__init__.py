from mpl.utils.scaffold.actions import copy,create

ACTIONS_DICT = {
    "CopyFile" : copy.copy_file,
    "CopyFolder" : copy.copy_folder,
    "EmptyFile" : create.empty_file, 
    "EmptyDir" : create.empty_dir, 
    "JsonFile" : create.json_file
}