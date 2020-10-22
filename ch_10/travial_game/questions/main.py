from player import Player
from question import Question
from trivia import Trivia

player_one = Player(input("Player 1 Name: "))
player_two = Player(input("Player 2 Name: "))

question = Question()
trivia_game = Trivia(player_one, player_two, question)
trivia_game.ask_question()
trivia_game.display_winner()
