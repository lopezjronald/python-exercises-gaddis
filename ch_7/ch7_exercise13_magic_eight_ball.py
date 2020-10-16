"""
13. Magic 8 Ball
Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
random response to a yes or no question. In the student sample programs for this book, you
will find a text file named 8_ball_responses.txt. The file contains 12 responses, such
as ?I don?t think so?, ?Yes, of course!?, ?I?m not sure?, and so forth. The program should
read the responses from the file into a list. It should prompt the user to ask a question, then
display one of the responses, randomly selected from the list. The program should repeat
until the user is ready to quit.

"""


def main():
    responses = generate_responses()
    ask_question()
    display_response(responses)


def ask_question():
    while True:
        question = input("Ask you questions: ")
        if question == '':
            print("No question asked.")
            continue
        else:
            print(question)
            break


def generate_responses():
    eight_ball_file = open('8_ball_responses.txt', 'r')
    eight_ball_responses = []
    for line in eight_ball_file:
        eight_ball_responses.append(line.strip())
    return eight_ball_responses


def display_response(responses):
    import random
    print(random.choice(responses))


main()
