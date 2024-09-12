import requests
from pprint import pprint as pp
# Importing html module - the questions returned from the API had encoded certain characters as HTML entities.
# The make the text more readable I imported the html module to do this.
import html
import time
# I also decided to use the emoji library to add a little more fun to the project. I installed with
# 'pip install emoji' and imported with the line below 'import emoji'
import emoji

# Welcome message
pp("*************************************************")
pp("*                                               *")
pp(emoji.emojize("*      :clapper_board:  WELCOME TO THE MOVIE QUIZ!  :clapper_board:       *"))
pp("*                                               *")
pp(emoji.emojize("*   - There are :keycap_10: true or false questions      *"))
pp(emoji.emojize("*   - Each correct answer gives you :keycap_1: point    *"))
pp("*   - Your result will be displayed and         *")
pp(emoji.emojize("*     output into a results.txt file  :file_folder:        *"))
pp(emoji.emojize("*   - Good luck!! :shamrock:                            *"))
pp("*                                               *")
pp("*************************************************")

# run_quiz function
def run_quiz():
    start_time = time.time()
    score = 0
    question_number = 1
    final_file = []
    # Loop to loop through data returned from API
    for y in data["results"]:
        # Question variable - fixing encoded html so question is more user-friendly and readable
        question = html.unescape(y["question"])
        correct_answer = y["correct_answer"]
        # Ensuring we have a boolean for the answer to compare further down in code
        if correct_answer == "True":
            correct_bool = True
        elif correct_answer == "False":
            correct_bool = False
        #     Code to handle any errors in data
        else:
            print(f"Error: Unrecognized correct answer {correct_answer}")
            question_number += 1
            continue

        # incorrect_answer = y["incorrect_answers"][0]
        # Question from data
        user_answer = input(f"{question_number}. Question: {question} \nEnter t for true or f for false: ")
        # code to only take in first letter of user answer, in case of error.
        user_answer = user_answer.strip().lower()[:1]
        # Setting boolean for users response
        if user_answer == "t":
            user_bool = True
        elif user_answer == "f":
            user_bool = False
        else:
            print("Invalid input. Please enter t for true or f for false.")
            continue
        # Comparing users answer and correct boolean to see if user is correct/incorrect
        if user_bool == correct_bool:
            score += 1
            print(emoji.emojize("Correct! :thumbs_up:"))
            # Adding question and answer to final file
            final_file.append(f"Question: {question}\nYour answer of {user_bool} was correct.")
        else:
            # print answer
            print(emoji.emojize(f"Wrong :thumbs_down:! The correct answer was: {y['correct_answer']}"))
            # Adding question and answer to final file
            final_file.append(f"Question: {question}\nYour answer of {user_bool} was incorrect.")
        question_number += 1

    if score <= 5:
        print(emoji.emojize(f"Hard luck! You have scored: {score}/10! :crying_face:"))
    elif score > 5:
        print(emoji.emojize(f"Excellent! You have scored: {score}/10! :clapping_hands:"))

    elapsed_time = time.time() - start_time
    # run save_results function with score and final file as arguments
    save_results(score, final_file, elapsed_time)

    return score

# save_results function which saves the score and final file to a .txt file
def save_results(score, final_file, elapsed_time):
    with open("results.txt", "w+") as text_file:
        # If score is < 50%, then give the text below
        if score <= 5:
            text_file.write("Better luck next time!!\n")
            text_file.write(f"You completed the quiz in {elapsed_time:.2f} seconds!\n\n")
        elif score > 5:
            # If score is above 50% then congratulate
            text_file.write("You're a movie genius!!\n")
            text_file.write(f"You completed the quiz in {elapsed_time:.2f} seconds!\n\n")
        text_file.write(f"Your final score is: {score}/10\n\n")
        text_file.write("\n".join(final_file))


# Asks user to start the quiz
# Default value to start
start_bool = None

# Loop until there is a valid response
while start_bool is None:
    user_input = input(emoji.emojize("Would you like to start the quiz :party_popper:? y for yes, n for no: ")).strip().lower()

    if user_input == "y":
        start_bool = True
    elif user_input == "n":
        start_bool = False
    else:
        print("Invalid input. Please enter y for yes or n for no.")

# I am using the Open Trivia DB API, which does not need an API key, and have generated the
# url below by stating I want an easy movie quiz, with multiple choice answers
endpoint = f"https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=boolean"
# Get quiz data from API
response = requests.get(endpoint)
# Puts json of data into data variable
data = response.json()
# print(data)


if start_bool == False:
    print("Come back when you want to take part in the quiz!")
elif start_bool == True:
    run_quiz()

