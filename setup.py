from setuptools import setup

APP = ['zzGUI.py']
DATA_FILES = ['features.json', "help.txt"]
OPTIONS = {
    'argv_emulation': False
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
