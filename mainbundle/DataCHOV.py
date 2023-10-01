import json, os
#Data checker/Overwriter

#vars
NoJsonData = 'undefined'
directory_path = os.path.dirname(os.path.realpath(__file__))
directory_path = os.path.join(directory_path, 'UidData.json')
userIDfound = False


def DataOverwriter(OverwriteMode):
    if OverwriteMode == True:
        UserInput = input("One of your IDS was undefined, check UidData.json and replace any ID missing/not defined (N/A) with the proper data. Optionally you can choose to overwrite the data from here. Overwrite data? (Y/N): ")
    elif OverwriteMode != True:

        UserInput = input("Overwrite Function called, type y to continue, type n to quit. (Y/N): ")
    if UserInput.lower() == 'yes' or UserInput.lower() == 'y':
        print('Overwriting data.')

        ###functions

        def ServerGuild():
            global ServerGuildID
            ServerGuildID = input('guild_id = ')

            UserInput = input("is " + ServerGuildID + " your guild/server id? (Y/N): ")

            if UserInput.lower() == 'yes' or UserInput.lower() == 'y':
                return
            else: ServerGuild()

        def ServerChannel():
            global ServerChannelID
            ServerChannelID = input('channel_id = ')

            UserInput = input("is " + ServerChannelID + " your preferred guild/server's channel id? (Y/N): ")

            if UserInput.lower() == 'yes' or UserInput.lower() == 'y':
                return
            else: ServerChannel()

        def BotToken():
            global BotTokenID
            BotTokenID = input('bot_token_id = ')

            UserInput = input("is "+BotTokenID+" your bot token id? (Y/N): ")

            if UserInput.lower() == 'yes' or UserInput.lower() == 'y':
                return
            else: BotToken()

        def TokenObscure():
            global BotTokenObscure
            BotTokenObscure = input('would you like ur bot token to be obscured when running Main? (Bool type, input either true or false ..): ')

            if BotTokenObscure == 'true':
                BotTokenObscure = True
            elif BotTokenObscure == 'false':
                BotTokenObscure = False

            UserInput = input("is "+str(BotTokenObscure)+" your bool input? (Y/N): ")
            if UserInput.lower() == 'yes' or UserInput.lower() == 'y':
                return
            else: TokenObscure

        ServerGuild()
        ServerChannel()
        BotToken()
        TokenObscure()
        JsonDICT = {
        "permissions": [
            {
        "guild_id": ServerGuildID,
        "channel_id": ServerChannelID,
        "token_id": BotTokenID,
        "token_ob": BotTokenObscure
            }
        ]
    }
    json_obj = json.dumps(JsonDICT, indent=4)
    with open(directory_path, "w") as file:
        file.write(json_obj)
    file.close()
    print("Data overwritten.")
    input("CMD will close after you press enter, relaunch the file if you ever need/want to change it or want to check your data.")
    exit(0)
def init():
    #try opening UserID and checking if the file exists.
    try:
        PathCheck = open(directory_path)
        PathCheck.close
        print("UidData.json was found!")
        global userIDfound
        userIDfound = True
    except FileNotFoundError:
        #once file was confirmed to not exist create the file and add undefined permissions
        print("File was not found! creating file")
        JsonDICT = {
            "permissions": [
                {
                "guild_id": NoJsonData,
                "channel_id": NoJsonData,
                "token_id": NoJsonData,
                "token_ob": NoJsonData
                }
            ]
        }
        json_obj = json.dumps(JsonDICT, indent=4)
        with open(directory_path, "w") as file:
           file.write(json_obj)
           file.close()
           input("relaunch this file!")
           exit(0)


def main():
    with open(directory_path, 'r+') as file:
        list = json.load(file)
        file.close()
        for item in list['permissions']:
            guild_id = item['guild_id']
            channel_id = item['channel_id']
            token_id = item['token_id']
            bot_token_obscure = item['token_ob']
            OverwriteMode = False
            if guild_id==NoJsonData or channel_id==NoJsonData or token_id==NoJsonData or bot_token_obscure==NoJsonData:
                OverwriteMode = True
                DataOverwriter(OverwriteMode)

            elif guild_id!=NoJsonData or channel_id!=NoJsonData or token_id!=NoJsonData or bot_token_obscure!=NoJsonData:
                if bot_token_obscure == True:
                    print("Guild ID: " + guild_id + "\nChannel ID: " + channel_id + "\nBot_Token: OBSCURED.")
                else:
                    print("Guild ID: " + guild_id + "\nChannel ID: " + channel_id + "\nBot_Token: " + token_id)
                UserInput = input("Do you wish to overwrite your data? (Y/N): ")
                global returned
                if UserInput.lower() == 'yes' or UserInput.lower() == 'y':
                    DataOverwriter(OverwriteMode)
                    returned = True
                else:
                    returned = False
