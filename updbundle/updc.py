import base64, os, requests, ctypes, subprocess, sys, webbrowser
from ctypes.wintypes import HWND, LPWSTR, UINT


headers = {}
gitversion = 'https://api.github.com/repos/Nixxty/Ergot.py/contents/version'
gitlink = 'https://github.com/Nixxty/Ergot.py'
r = requests.get(gitversion, headers=headers)
r.raise_for_status()
data = r.json()
file_con = data['content']
dir_p = os.path.dirname(os.path.realpath(__file__))
dir_p = os.path.join(dir_p, 'version')
with open(dir_p, 'r') as f:
    vdata = f.read()
    f.close()
deco_con = file_con = base64.b64decode(file_con).decode()
gitdecon = deco_con.split('\n')
vercon = vdata.split('\n')

_user32 = ctypes.WinDLL('user32', use_last_error=True)

_MessageBoxW = _user32.MessageBoxW
_MessageBoxW.restype = UINT  # default return type is c_int, this is not required
_MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

YESNO = 0x04
IDYES = 6
IDNO = 7

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



def mainbox():
    try:
        result = Mbox(None, 'Would you like to update to version: '+(gitdecon[0])+'?\n\nupdate time: '+(gitdecon[1]), 'Ergot UPD Confirmation', YESNO)
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
    print("local version: "+vercon[0]+"\nlocal update time: "+vercon[1]+"\n\ngit version: " + gitdecon[0]+ "\ngit update time: " + gitdecon[1])
    if gitdecon[0] and vercon[0] == gitdecon[0]:
        print("up to date!")
    elif gitdecon[0] and vercon[0] != gitdecon[0]:
        print("Update available.")
        mainbox()