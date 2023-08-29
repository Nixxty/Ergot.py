import json, os
#Data checker/Overwriter

#vars
mid = 'undefined'
dir_p = os.path.dirname(os.path.realpath(__file__))
dir_p = os.path.join(dir_p, 'UidData.json')
uidfound = False
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
                    btid = input('bot_token_id = ')
                    uinput = input("is "+btid+" your bot token id? (Y/N): ")
                    if uinput.lower() == 'yes' or uinput.lower() == 'y':
                        btob = input('would you like ur bot token to be obscured when running Main? (Bool type, input either true or false ..): ')
                        if btob == 'true':
                            btob = True
                        elif btob == 'false':
                            btob = False
                        uinput = input("is "+str(btob)+" your bool input? (Y/N): ")
                        if uinput() == 'yes' or uinput.lower() == 'y':
                            dictionary = {
                            "permissions": [
                                {
                            "guild_id": tgid,
                            "channel_id": tcid,
                            "token_id": btid,
                            "token_ob": btob
                                }
                            ]
                        }
                        json_obj = json.dumps(dictionary, indent=4)
                        with open(dir_p, "w") as g:
                            g.write(json_obj)
                        g.close()
                        print("Data overwritten.")
                        input("CMD will close after you press enter, relaunch the file if you ever need/want to change it or want to check your data.")
                        exit(0)
def init():
    #try opening Uid and checking if the file exists.
    try:
        f = open(dir_p)
        f.close
        print("UidData.json was found!")
        global uidfound
        uidfound = True
    except FileNotFoundError:
        #once file was confirmed to not exist create the file and add undefined permissions
        print("File was not found! creating file")
        dictionary = {
            "permissions": [
                {
                "guild_id": mid,
                "channel_id": mid,
                "token_id": mid,
                "token_ob": mid
                }
            ]
        }
        json_obj = json.dumps(dictionary, indent=4)
        with open(dir_p, "w") as g:
           g.write(json_obj)
           g.close()
           input("relaunch this file!")
           exit(0)


def main():
    with open(dir_p, 'r+') as f:
        data = json.load(f)
        f.close()
        for i in data['permissions']:
            guild_id = i['guild_id']
            channel_id = i['channel_id']
            token_id = i['token_id']
            bot_token_obscure = i['token_ob']
            mib = False
            if guild_id==mid or channel_id==mid or token_id==mid or bot_token_obscure==mid:
                mib = True
                DataOV(mib)

            elif guild_id!=mid or channel_id!=mid or token_id!=mid or bot_token_obscure!=mid:
                if bot_token_obscure == True:
                    print("Guild ID: " + guild_id + "\nChannel ID: " + channel_id + "\nBot_Token: OBSCURED.")
                else:
                    print("Guild ID: " + guild_id + "\nChannel ID: " + channel_id + "\nBot_Token: " + token_id)
                uinput = input("Do you wish to overwrite your data? (Y/N): ")
                if uinput.lower() == 'yes' or uinput.lower() == 'y':
                    DataOV(mib)