from player import Player
from chat_message import Chat_Message
class info:
    def __init__(self, get_request_output):
        self.data = get_request_output
        self.process_data()

    def process_data(self):
        #Server information
        self.playerCount = str(self.data["currentcount"])
        self.hasStorm = self.data["hasStorm"]
        self.hasThunder = self.data["isThundering"]
        self.time = str(self.data["servertime"])
        self.timeStamp = str(self.data["timestamp"])

        #Player_info
        self.players = []
        for i in range(int(self.playerCount)):
            player_data = self.data["players"][i]
            self.players.append(Player(player_data))

        #Chat
        self.chat_messages = []
        self.join_or_leave = []
        for i in range(len(self.data["updates"])):
            if self.data["updates"][i]["type"] == "chat":
                self.chat_messages.append(Chat_Message(self.data["updates"][i]))
            elif self.data["updates"][i]["type"] == "playerjoin":
                self.join_or_leave.append([self.timeStamp, self.data["updates"][i]["playerName"], "join"])
            elif self.data["updates"][i]["type"] == "playerquit":
                self.join_or_leave.append([self.timeStamp, self.data["updates"][i]["playerName"], "quit"])

    def generate_csv_string(self, separator1, separator2):
        #Stored as timeStamp, playerCount, hasStorm, hasThunder, servertime
        output = separator1.join([self.timeStamp, self.playerCount, str(self.hasStorm), str(self.hasThunder), self.time]) + separator2
        return output