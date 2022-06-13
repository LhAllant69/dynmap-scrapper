class Chat_Message:
    def __init__(self, chat_data):
        self.data = chat_data
        self.process_data()
    
    def process_data(self):
        self.sender = str(self.data["playerName"])
        self.content = str(self.data["message"])
        self.timeStamp = str(self.data["timestamp"])

    def generate_csv_string(self, separator1, separator2):
        #Stored as timeStamp, sender, content
        output = separator1.join([self.timeStamp, self.sender, self.content]) + separator2
        return output