import os

Directory_Path = os.path.dirname(os.path.realpath(__file__))
Directory_Path = os.path.join(Directory_Path, 'requirements.txt')
def setup():
    os.system(f"py -m pip install -r {Directory_Path}")
setup()