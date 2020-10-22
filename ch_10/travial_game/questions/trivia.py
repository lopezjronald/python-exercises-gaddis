class Trivia:

    def __init__(self, Player_One, Player_Two, Question):

        self.__player_1 = Player_One
        self.__player_2 = Player_Two
        self.__question = Question

    def ask_question(self):
        player = self.__player_1.get_player_name()
        for key, value in self.__question.get_question_dictionary().items():
            print(player.title())
            count = 1
            print(f"{key}")
            list_of_answers = list(value.values())[0]
            for possible_answer in list_of_answers:
                print(f"{count}: {possible_answer}")
                count += 1
            while True:
                try:
                    player_choice = int(input("Please choose from the following choices (1 - 4)\n"))
                    break
                except ValueError:
                    print("Invalid entry")
            player_choice = list_of_answers[player_choice - 1]
            correct_answer = list(value.keys())[0]
            if player_choice == correct_answer:
                print("Correct")
                if player == self.__player_1.get_player_name():
                    self.__player_1.add_point(1)
                else:
                    self.__player_2.add_point(1)
            else:
                print("Incorrect")
            if player == self.__player_1.get_player_name():
                player = self.__player_2.get_player_name()
            else:
                player = self.__player_1.get_player_name()
            print(f"Player Choice: {player_choice}\nCorrect Answer: {correct_answer}")

    def display_winner(self):
        print(f"{self.__player_1.get_player_name()}: {self.__player_1.get_player_points()} points")
        print(f"{self.__player_2.get_player_name()}: {self.__player_2.get_player_points()} points")
        if self.__player_1.get_player_points() == self.__player_2.get_player_points():
            print("Draw")
        elif self.__player_1.get_player_points() > self.__player_2.get_player_points():
            print(
                f"{self.__player_1.get_player_name().title()} wins by {self.__player_1.get_player_points() - self.__player_2.get_player_points()} points.")
        else:
            print(
                f"{self.__player_2.get_player_name().title()} wins by {self.__player_2.get_player_points() - self.__player_1.get_player_points()} points.")
