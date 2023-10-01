import base64, os, requests, ctypes, subprocess, sys, webbrowser
from ctypes.wintypes import HWND, LPWSTR, UINT

### Version file from Github
headers = {}
gitversion = 'https://api.github.com/repos/Nixxty/Ergot.py/contents/updbundle/version'
gitlink = 'https://github.com/Nixxty/Ergot.py'
githubversionfile = requests.get(gitversion, headers=headers)
githubversionfile.raise_for_status()
### turning github version file into a list var
data = githubversionfile.json()
gitfile_content = data['content']
### Grabbing local version files content
Directory_Path = os.path.dirname(os.path.realpath(__file__))
Directory_Path = os.path.join(Directory_Path, 'version')
with open(Directory_Path, 'r') as f:
    LocalVersionData = f.read()
    f.close()
### Dechipering Github version B64 to ASCII
gitdecoded_content = gitfile_content = base64.b64decode(gitfile_content).decode()
GitDecodedContentAsList = gitdecoded_content.split('\n')
LocalVersionContent = LocalVersionData.split('\n')
### Removing any whitespace from string (iirc)
GitDecodedContentAsList[0] = GitDecodedContentAsList[0].strip()
GitDecodedContentAsList[1] = GitDecodedContentAsList[1].strip()
LocalVersionContent[0] = LocalVersionContent[0].strip()
LocalVersionContent[1] = LocalVersionContent[1].strip()


### Message box stuff
_user32 = ctypes.WinDLL('user32', use_last_error=True)

_MessageBoxW = _user32.MessageBoxW
_MessageBoxW.restype = UINT  # default return type is c_int, this is not required
_MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

YESNO = 0x04
IDYES = 6
IDNO = 7


### msg box function
def Mbox(hwnd, title, text, utype):
    result = _MessageBoxW(hwnd, title, text, utype)
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return result

def httpslinkstart(gitlink):
    url = gitlink
    if sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    else:
        webbrowser.open_new_tab(url)


### Update available function, asks user if they would like a link to the github to open.
def mainbox():
    try:
        result = Mbox(None, 'Would you like to update to version: '+(GitDecodedContentAsList[0])+'?\n\nupdate time: '+(GitDecodedContentAsList[1]), 'Ergot UPD Confirmation', YESNO)
        if result == IDYES:
            print("pressed yes")
            httpslinkstart(gitlink=gitlink)
        elif result == IDNO:
            print("pressed no")
        else:
            print("unknown return code")
    except WindowsError as win_err:
        print("an error occured:\n".format(win_err))

def maincheck():
    print("local version: "+LocalVersionContent[0]+"\nlocal update time: "+LocalVersionContent[1]+"\n\ngit version: " + GitDecodedContentAsList[0]+ "\ngit update time: " + GitDecodedContentAsList[1])
    if LocalVersionContent[0] == GitDecodedContentAsList[0]:
        print("up to date!")
    elif LocalVersionContent[0] != GitDecodedContentAsList[0]:
        print("Update available.")
        mainbox()
