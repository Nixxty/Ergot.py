#main file, runs everything from this single file including datachov and bot file.

from mainbundle import DataCHOV
from updbundle import updc
import dependencies
updc.maincheck()
dependencies.dep()
def mainop():
    uinput = input("\nRun bot = 1\nrun Data checker/overwriter = 2\noptions: 1 | 2\n")
    if uinput == '1':
        print('running bot.')
        from mainbundle import bot
    elif uinput == '2':
        DataCHOV.init()
        if DataCHOV.uidfound == True:
            DataCHOV.main()
            if DataCHOV.returned == False:
                mainop()
mainop()
