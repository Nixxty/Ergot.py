#main file, runs everything from this single file including datachov and bot file.
from mainbundle import DataCHOV
from updbundle import setup, updc
from mainbundle.exts.cmds import clearterminal
args = ['1','2'] #arguments for if statements lower in the code, was used in hopes of making the code more readable.

setup.setup()
clearterminal(1,3)
updc.maincheck()
clearterminal(1,3)
## if passed check

def Selector():
    clearterminal(0,2)
    UserInput = input("Run bot = 1\nrun Data checker/overwriter = 2\noptions: 1 | 2\n\n")

    if UserInput == args[0]: #BOTRUN
        clearterminal(0,0)
        from mainbundle import bot

    elif UserInput == args[1]: #DATACHOV RUN

        DataCHOV.init()
        if DataCHOV.userIDfound == True:
            clearterminal(0,1)
            DataCHOV.main()
            if DataCHOV.returned == False:
                Selector()

    if UserInput != args: #RESTART SELECTOR IF NOT EQUAL TO CORRECT ARG
        Selector()
Selector()
