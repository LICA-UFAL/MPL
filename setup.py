from setuptools import setup, find_packages
from setuptools.command.install import install

from mpl import __version__
from mpl.utils.version import get_version
from mpl.scripts.builder import builde_mpl_cache_folder

class InstallWrapper(install):
    """
    Provide an install wrapper that run all of builder processing.
    """

    def run(self):
        install.run(self)
        builde_mpl_cache_folder()


setup(
    name='mpl',
    version=get_version(__version__),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mpl=mpl.scripts.main:cli
    ''',
    cmdclass={'install': InstallWrapper},
)