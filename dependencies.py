import sys
import subprocess
import pkg_resources
#checks and downloads modules necessary for the project to work.
dependencies = {'discord', 'GPUtil', 'psutil', 'datetime', 'desktopmagic'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = dependencies - installed
def dep():
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)