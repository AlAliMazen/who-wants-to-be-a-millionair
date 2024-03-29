import gspread
from google.oauth2.service_account import Credentials
import random
from question import Question
import re
import os               # to detect the operating system
import platform         # to detect the platform Windows, Linux , macOS or ...
import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('who_wants_to_be_a_millionair')


def split_list(list, single_question):
    """
    for making sublist of the big questions list
    """
    return [list[i:i + single_question] for i in range(0, len(list), single_question)]  # noqa


def read_file(file):
    """
    reading the content of  txt file which contains the questions
    and return a list of lists from the questions
    """
    print("Reading questions")
    content = []
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            content.append(line.strip())  # Stripping '\n' character from each line  # noqa

        questions = split_list(content, 6)
        return questions


def print_game_title():
    """
    when starting, restarting or cleaning the console, the title will be printed  # noqa
    """
    padding = 15
    print("\n\n\n")
    print(" ".rjust(padding)+"|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|".ljust(padding))  # noqa
    print(" ".rjust(padding)+"|      WHO WANTS TO BE A MILLIONAIRE          |".ljust(padding))  # noqa
    print(" ".rjust(padding)+"|_____________________________________________|".ljust(padding)+"\n\n")  # noqa


def print_game_menu():
    """
    Greeting the user and show the Game menu
    """
    print_game_title()
    padding = 15
    print(" ".rjust(padding)+"1 ) Start the game")
    print(" ".rjust(padding)+"2 ) How to play this game (show instructions)?")
    print(" ".rjust(padding)+"3 ) Show Scoring Board")
    print(" ".rjust(padding)+"4 ) Quit\n\n")


def show_game_instructions():
    """
    print game instructions
    """
    clear_console()
    print_game_title()
    padding = 5
    print(" ".ljust(padding)+"This game start by asking you to type your fullname and country.")  # noqa
    print(" ".ljust(padding)+"These information will be saved in a database and used for")  # noqa
    print(" ".ljust(padding)+"scoring comparisons.\n")
    print(" ".ljust(padding)+"After typing your fullname and country, the game starts ")  # noqa
    print(" ".ljust(padding)+"to show 15 questions after each other and every question ")  # noqa
    print(" ".ljust(padding)+"has four choices 1 to 4 . You can type your choice as ")  # noqa
    print(" ".ljust(padding)+"digits not letters.\n")
    print(" ".ljust(padding)+"If your choice is correct, then you get 100 $ (virtually).")  # noqa
    print(" ".ljust(padding)+"Otherwise, you will lose the round and will be asked whether")  # noqa
    print(" ".ljust(padding)+"you want to play again or just finish the game by typing")  # noqa
    print(" ".ljust(padding)+"y for Yes or n for No.\n")
    print(" ".ljust(padding)+"Best wishes\n\n")


def get_user_choice():
    """
    used to get the user choice when instructions are show and user wants  # noqa 
    either to finish or start the game
    """
    while True:
        choice = input("For Menu press Y  To finish the Game E\nYour input: \n")  # noqa
        if choice.lower() == "e":
            print("choice is e or E")
            return "e"
        elif choice.lower() == "y":
            print("Showing the Game main\n")
            clear_console()
            return "y"
        else:
            print("Invalid choice either Y or E n")


def clear_console():
    """
    cleaning the console and give more clear UI to the game
    """
    system = platform.system()
    if system == "Windows":
        return os.system('cls')
    elif system == "Linux":
        return os.system('clear')
    elif system == "Darwin":
        return os.system('clear')


def get_player_data():
    """
    get player fullname, country, email and birth year
    """
    player_data = []
    while True:
        fullname = input("Enter your fullname please as John smith for example\n")  # noqa
        if validate_string_input(fullname.strip(), "Fullname"):
            player_data.append(fullname)
            break
    while True:
        country = input("Where are you from?\n")
        if validate_string_input(country.strip(), "Country"):
            player_data.append(country)
            break
    return player_data


def validate_string_input(str_input, type):
    """
    using RegEx regular expression to evaluate the name of the user
    """
    pattern = r'^[a-zA-Z ]+$'
    print("in validating string method "+str_input)
    try:
        if len(str_input) == 0:
            raise ValueError(f"{type} can't be empty")
        elif not re.match(pattern, str_input):
            raise ValueError(f"{type}  can only have letters both in lower and uppercase and spaces NO  # noqa numeric values!")
    except ValueError as e:
        print(f"Invalid input: {e}, please try again\n")
        return False

    return True


def validate_integer_input(usr_choice):
    """
    return False if the user input is less than 0 or grater than 4 or letters
    """
    pattern = r'^[1-4]$'
    print("User question choice: "+usr_choice)

    try:
        if not bool(re.match(pattern, usr_choice)):
            raise ValueError(f'{usr_choice} is not a valid choice \n')
    except ValueError as e:
        print(f"Invalid Choice: {e}")
        return False

    return True


def update_questions_worksheet(question_level, questions_list):
    """
    used when reading questions from text files and update the questions  # noqa
    worksheets i.e. population the google worksheet.
    """
    questions = SHEET.worksheet(question_level)
    data = questions.get_all_values()
    if len(data) == 1:
        print(f'update{question_level} worksheet ...\n')
        questions.append_rows(questions_list)
        print(f'{question_level} worksheet was updated successfully\n')
    else:
        print(f'{question_level} worksheet has already populated with questions\n')  # noqa


def read_questions_txt_files():
    """
    Used only one time to populate the Google sheet with the questions
    It won't don anything if the google sheet has questions already.
    """
    current_directory = os.getcwd()
    easy_questions = current_directory+"/easy-questions.txt"
    easy_questions = read_file(easy_questions)
    update_questions_worksheet("easy_questions", easy_questions)
    medium_questions = current_directory+"/medium-questions.txt"
    medium_questions = read_file(medium_questions)
    update_questions_worksheet("medium_questions", medium_questions)
    hard_questions = current_directory+"/hard-questions.txt"
    hard_questions = read_file(hard_questions)
    update_questions_worksheet("hard_questions", hard_questions)


def get_random_question_index(questions_list):
    """
    get a random index which represents the question row starting at one to
    exclude the headings till the last question
    """
    selected_question_ist = []
    while len(selected_question_ist) < 5:
        index = random.randint(1, len(questions_list)-1)
        if index not in selected_question_ist:
            selected_question_ist.append(index)

    return selected_question_ist


def get_questions_ready():
    """
    prepare 15 randomly selected question and collect them in a list
    """
    easy_questions = SHEET.worksheet("easy_questions").get_all_values()
    medium_questions = SHEET.worksheet("medium_questions").get_all_values()
    hard_questions = SHEET.worksheet("hard_questions").get_all_values()
    easy_questions_indices = get_random_question_index(easy_questions)
    medium_questions_indices = get_random_question_index(medium_questions)
    hard_questions_indices = get_random_question_index(hard_questions)

    all_player_questions = []

    for question in easy_questions_indices:
        single_question = easy_questions[question]
        all_player_questions.append(single_question)

    for question in medium_questions_indices:
        single_question = medium_questions[question]
        all_player_questions.append(single_question)

    for question in hard_questions_indices:
        single_question = hard_questions[question]
        all_player_questions.append(single_question)

    return all_player_questions


def get_question(index):
    """
    initialize a question object and return it back
    """
    question_obj = Question(index)
    return question_obj


def print_question_with_choices(question, index):
    """
    print the question in certain style inside the question
    """
    padding = 10
    print(f' '.ljust(padding)+str(index+1)+" "+question.get_question_txt().ljust(padding)+'')  # noqa
    print(f''.ljust(1)+"".center(len(str(index+1)+question.get_question_txt())+padding*2, "-")+'')  # noqa
    print(f''.ljust(padding//2)+'1 ) '+question.get_question_option(1).ljust(padding*2)+' 3 ) '+question.get_question_option(3))  # noqa
    print(f''.ljust(padding//2)+'2 ) '+question.get_question_option(2).ljust(padding*2)+' 4 ) '+question.get_question_option(4))  # noqa
    print("\n\n")


def print_player_info(player, q_index):
    """
    Show the current player information at the top of the Game UI
    """
    level = "Easy"
    if q_index > 10:
        level = "Hard"
    elif q_index > 5:
        level = "Medium"
    print(f'Player name:{player[0]}   Country: {player[1]}   Score {player[2]}   Level: {level}')  # noqa


def update_scoring_sheet(player, index):
    """
    called when player loses the round to update the sheet.
    """
    level = 'Easy'
    if index > 10:
        level = 'Hard'
    elif index > 5:
        level = 'Medium'
    now = datetime.datetime.now().strftime("%d.%m.%Y")
    scoring = []
    for ind in player:
        scoring.append(ind)
    scoring.append(level)
    scoring.append(now)
    scoring_sheet = SHEET.worksheet("scoring")
    scoring_sheet.append_row(scoring)


def print_winner_info(player, index):
    """
    print the winner information to the console
    update the database
    """
    level = 'Easy'
    if index > 10:
        level = 'Hard'
    elif index > 5:
        level = 'Medium'
    now = datetime.datetime.now().strftime("%d.%m.%Y")
    print(" ".rjust(25)+"Congratulations ! You are a millionaire now")
    print(' '.rjust(15)+"Fullname: "+player[0]+' Country: '+player[1]+' Score: '+str(player[2])+" Date: "+now)  # noqa
    update_scoring_sheet(player, index)


def get_scoring_board():
    """
    print the Scoring Board from google sheet
    """
    scoring_sheet = SHEET.worksheet('scoring').get_all_values()
    scoring_sheet = scoring_sheet[1:]
    scores_as_integers = [[sublist[0], sublist[1], int(sublist[2]), sublist[3], sublist[4]] for sublist in scoring_sheet]  # noqa
    sorted_data = sorted(scores_as_integers, key=lambda x: x[2], reverse=True)
    gap = 10
    clear_console()
    print_game_title()
    print("".rjust(gap//2)+"Full name".ljust(gap*2)+"Country".ljust(gap)+"Score".ljust(gap)+"Level".ljust(gap)+"Date".ljust(gap)+"\n")  # noqa

    for row in sorted_data:
        print("".rjust(gap//2)+row[0].ljust(gap*2)+row[1].ljust(gap)+str(row[2]).ljust(gap)+row[3].ljust(gap)+row[4].ljust(4))  # noqa

    print("\n\n\n")


def play_again_mechanism(player_obj):
    """
    Asking player if s/he play again.                               # noqa
    param: player_obj: is choice is yes the score should be reset
    """
    while True:
        second_round = input("Do you want to play again\n Y for yes N for No\n")  # noqa
        if str.lower(second_round) == "y":
            player_obj.play_again()
            return True
        elif str.lower(second_round) == "n":
            return False
        else:
            print("Invalid choice.\n\n")


def end_game_message():
    """
    print farewell message when quitting game or losing the round
    """
    clear_console()
    padding = 15
    print("\n\n\n")
    print(" ".ljust(padding)+"Thank you very much for trying this Game")
    print("\n")
    print(" ".ljust(padding)+"Best wishes next time")
    print("\n\n\n")
