import json, os
mid = 'undefined'
def DataOV(mib):
    if mib == True:
        uinput = input("One of your IDS was undefined, check UidData.json and replace any ID missing/not defined (N/A) with the proper data. Optionally you can choose to overwrite the data from here. Overwrite data? (Y/N): ")
    elif mib != True:
        uinput = input("Overwrite Function called, type y to continue, type n to quit. (Y/N): ")
    if uinput.lower() == 'yes' or uinput.lower() == 'y':
        print('Overwriting data.')
        tgid = input('guild_id = ')
        uinput = input("is " + tgid + " your guild/server id? (Y/N): ")
        if uinput.lower() == 'yes' or uinput.lower() == 'y':
            tcid = input('channel_id = ')
            uinput = input("is " + tcid + " your preferred guild/server's channel id? (Y/N): ")
            if uinput.lower() == 'yes' or uinput.lower() == 'y':
                taid = input('auth_id = ')
                uinput = input("is " + taid + " your discord user id? (Y/N): ")
                if uinput.lower() == 'yes' or uinput.lower() == 'y':
                    dictionary = {
                        "permissions": [
                            {
                        "guild_id": tgid,
                        "channel_id": tcid,
                        "auth_id": taid
                            }
                        ]
                    }
                    json_obj = json.dumps(dictionary, indent=3)
                    with open("UidData.json", "w") as g:
                        g.write(json_obj)
                    g.close()
                    print("Data overwritten.")
                    input("CMD will close after you press enter, relaunch the file if you ever need/want to change it and or want to check your data.")
def init():
    try:
        f = open('UidData.json')
        f.close
        print("UidData.json was found!")
        main()
    except FileNotFoundError:
        print("File was not found! creating file")
        dictionary = {
            "permissions": [
                {
                "guild_id": mid,
                "channel_id": mid,
                "auth_id": mid
                }
            ]
        }
        json_obj = json.dumps(dictionary, indent=3)
        with open("UidData.json", "w") as g:
           g.write(json_obj)
           g.close()
           input("relaunch this file!")
           exit(0)


def main():
    with open('UidData.json', 'r+') as f:
        data = json.load(f)
        f.close()
        for i in data['permissions']:
            guild_id = i['guild_id']
            channel_id = i['channel_id']
            auth_id = i['auth_id']
            mib = False
            if guild_id==mid or channel_id==mid or auth_id==mid:
                mib = True
                DataOV(mib)
            elif guild_id!=mid or channel_id!=mid or auth_id!=mid:
                print("Guild ID: " + guild_id + "Channel ID: " + channel_id + "Auth_ID: " + auth_id)
                uinput = input("Do you wish to overwrite your data? (Y/N): ")
                if uinput.lower() == 'yes' or uinput.lower() == 'y':
                    DataOV(mib)
init()