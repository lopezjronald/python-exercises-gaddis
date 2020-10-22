class Player:
    def __init__(self, name):
        self.__player_name = name
        self.__player_points = 0

    def get_player_name(self):
        return self.__player_name

    def get_player_points(self):
        return self.__player_points

    def add_point(self, point):
        self.__player_points += point
