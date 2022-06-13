class Player:
    def __init__(self, player_data):
        self.data = player_data
        self.process_data()

    def process_data(self):
        self.world = self.data["world"]
        self.position = str(self.data["x"]), str(self.data["y"]), str(self.data["z"])
        self.health = str(self.data["health"])
        self.armor = str(self.data["armor"])
        self.name = str(self.data["name"])

    def generate_position_string(self, separator):
        return "{}{}{}{}{}".format(self.position[0], separator, self.position[1], separator, self.position[2])

    def generate_csv_string(self, separator1, separator2, timeStamp):
        #Stored as timeStamp, world, position, health, armor
        output = separator1.join([timeStamp, self.world, self.generate_position_string(separator1), self.health, self.armor]) + separator2
        return output