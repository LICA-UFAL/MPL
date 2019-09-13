import os
from distutils.dir_util import copy_tree

from mpl.utils.scaffold.scaffold import Scaffold
from mpl.settings import MPL_CACHE_PATH, MPL_CACHE_SCAFFOLD_PATH

# post installation script
def builde_mpl_cache_folder():
    """ Create mpl cache folder, copping scaffolds and saving config files. """
    
    Scaffold.load_from_file(MPL_CACHE_SCAFFOLD_PATH).run(MPL_CACHE_PATH)
