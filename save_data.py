import os
import utils

separator1 = "\t"
separator2 = "\n"

path = "data//"
endpoints = {
    "chat":"chat.csv",
    "player":"player//",
    "other":"server_status.csv",
    "join_or_leave":"join_or_leave.csv"
}
def save(info_object):
    timeStamp = info_object.timeStamp
    #Chat
    #Append the chat file
    #Chat is in csv format with \n as a separator and \t as a sub separator
    for i in info_object.chat_messages:
        utils.append_file(path + endpoints["chat"], i.generate_csv_string(separator1, separator2))

    #Players
    for i in info_object.players:
        utils.append_file(path + endpoints["player"] + i.name + ".csv", i.generate_csv_string(separator1, separator2, timeStamp))
    
    #general things
    utils.append_file(path + endpoints["other"], info_object.generate_csv_string(separator1, separator2))

    #Player joins or leave
    for i in info_object.join_or_leave:
        utils.append_file(path + endpoints["join_or_leave"], separator1.join(i) + separator2)