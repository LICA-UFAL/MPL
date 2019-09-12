import os
from distutils.dir_util import copy_tree

from mpl.settings import MPL_CACHE_PATH, SCAFFOLDS_FOLDER_PATH


INSTALL_SCAFFOLDS_FILE_PATH = "mpl/scaffolds"

# post installation script
def builde_mpl_cache_folder():
    """ Create mpl cache folder, copping scaffolds and saving config files. """

    if not os.path.exists(MPL_CACHE_PATH):
        os.makedirs(MPL_CACHE_PATH)

    copy_scaffolds_files()

def copy_scaffolds_files():
    """ Copy all default scaffold config files to cache path. """

    copy_tree(INSTALL_SCAFFOLDS_FILE_PATH, SCAFFOLDS_FOLDER_PATH)