import os

from functools import partial
from mpl.utils.functions import pipe
from mpl.utils.file import read_file_to_dict
from mpl.utils.scaffold.actions.create import empty_dir
from mpl.utils.scaffold.actions import ACTIONS_DICT

ACCEPTED_SCAFFOLD_FILE_FORMATS = [".json"]

class Scaffold():
    def __init__(self, name, file_tree_dict, scaffold_file_path = None):
        self.name = name 
        self.file_tree_dict = file_tree_dict
        self.scaffold_file_path = scaffold_file_path
    
    def run(self, destination_path):
        self.__interpreter_dict(destination_path, self.file_tree_dict)

    def update_file_tree(self, key, value):
        self.file_tree_dict[key] = value

    def __interpreter_dict(self, curr_path, file_tree_dict):

        empty_dir(curr_path)
        for key, value in file_tree_dict.items():
            if isinstance(value, dict):
                self.__interpreter_dict(os.path.join(curr_path, key), value)
            elif isinstance(value, list) and key in ACTIONS_DICT:
                ACTIONS_DICT[key](curr_path, *value)
            else:
                raise Exception("Coud not read the scaffold in {0}, please chech the file text format". \
                                format(self.scaffold_file_path))

    def __str__(self):
        return str(self.name)

    @classmethod
    def load_from_file(cls, file_path):
        """ Create an scaffold object from file """

        dict_file = read_file_to_dict(file_path)

        if "name" in dict_file and "tree" in dict_file:
            return Scaffold(dict_file["name"], dict_file["tree"], file_path)
        else:
            return None

    @classmethod
    def load_scaffolds_from_folder(cls, folder_path):
        """  Return an list of scaffold object for every scaffold file in folder_path """
        
        load_scaffolds = pipe(
            os.listdir,
            partial(map, partial(os.path.join, folder_path)),
            partial(filter, os.path.isfile), 
            partial(filter, lambda file_path: os.path.splitext(file_path)[-1]
                     in ACCEPTED_SCAFFOLD_FILE_FORMATS),
            partial(map, cls.load_from_file),
            partial(filter, None),
            list
        )

        return load_scaffolds(folder_path)