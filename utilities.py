import gspread
from google.oauth2.service_account import Credentials
import random
from pprint import pprint
from question import Question
import re

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
    return [list[i:i + single_question] for i in range(0, len(list), single_question)]


def read_file(file):
    """
    reading the content of  txt file which contains the questions
    and return a list of lists from the questions
    """
    print( "Reading questions")
    content=[]
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            content.append(line.strip())  # Stripping '\n' character from each line
        
        questions=split_list(content,6)
        return questions

def print_game_title():
    """
    when starting, restarting or cleaning the console, the title will be printed 
    """
    padding=15
    print(" ".rjust(padding)+"|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|".ljust(padding))
    print(" ".rjust(padding)+"|      WHO WANTS TO BE A MILLIONAIRE          |".ljust(padding))
    print(" ".rjust(padding)+"|_____________________________________________|".ljust(padding)+"\n\n")

def print_game_menu():
    """
    Greeting the user and show the Game menu
    """
    print_game_title()
    padding=15
    print(" ".rjust(padding)+"1 ) How to play this game (show instructions)?")
    print(" ".rjust(padding)+"2 ) Start the game")
    print(" ".rjust(padding)+"3 ) Quite\n\n")


def show_game_instructions():
    """
    print the instruction 
    """
    padding=15
    print(" ".rjust(padding)+"This game start by asking you to type your fullname and country. These information will be saved")
    print(" ".rjust(padding)+"in a database and used for scoring comparisons.\n\n")
    print(" ".rjust(padding)+"After typing your fullname and country, the game starts to show 15 questions after each other and every")
    print(" ".rjust(padding)+"question has four choices 1 to 4 . You can type your choice as digits not letters.\n")
    print(" ".rjust(padding)+"If your choice is correct, then you get 100 $ (virtually). Otherwise, you will lose the round and ")
    print(" ".rjust(padding)+"will be asked whether you want to play again or just finish the game by typing y for Yes or n for No.\n")
    print(" ".rjust(padding)+"Best wishes\n\n")

def get_player_data():
    """
    get player fullname, country, email and birth year
    """
    player_data=[]
    while True:
        fullname=input("Enter your fullname please as John smith for example\n")
        if validate_string_input(fullname,"Fullname"):
            player_data.append(fullname)
            break
    while True:
        country=input("Where are you from?\n")
        if validate_string_input(country,"Country"):
            player_data.append(country)
            break
    return player_data


def validate_string_input(str_input,type):
    """
    using RegEx regular expression to evaluate the name of the user
    """
    pattern = r'^[a-zA-Z ]+$'
    try:
        if len(str_input)==0 :
            raise ValueError(f"{type} can't be empty")
        elif not re.match(pattern, str_input):
            raise ValueError(f"{type}  can only have letters both in lower and uppercase and spaces NO numeric values!")        
    except ValueError as e:
        print(f"Invalid input: {e}, please try again\n")
        return False
    
    return True


def validate_integer_input(usr_choice):
    pattern=r'^[1-4]$'
    try:
        if not bool(re.match(pattern,usr_choice)):
            print("it is here")
            raise ValueError(f'{usr_choice} is not a valid choice \n')
    except ValueError as e:
        print(f"Invalid Choice: {e}")
        return False
    
    return True


def update_questions_worksheet(question_level, questions_list):
    questions=SHEET.worksheet(question_level)
    data=questions.get_all_values()
    if len(data)==1:
        print(f'update{question_level} worksheet ...\n')
        questions.append_rows(questions_list)
        print(f'{question_level} worksheet was updated successfully\n')
    else:
        print(f'{question_level} worksheet has already populated with questions\n')


def get_random_question_index(questions_list):
    """
    get a random index which represents the question row starting at one to 
    exclude the headings till the last question
    """
    selected_question_ist=[]
    while len(selected_question_ist)<5:
        index=random.randint(1,len(questions_list)-1)
        if not index in selected_question_ist:
            selected_question_ist.append(index)
    
    return selected_question_ist 

def get_questions_ready():
    """
    prepare 15 randomly selected question and collect them in a list
    """
    easy_questions=SHEET.worksheet("easy_questions").get_all_values()
    medium_questions=SHEET.worksheet("medium_questions").get_all_values()
    hard_questions=SHEET.worksheet("hard_questions").get_all_values()
    
    #collect index in sets to avoid duplicates
    easy_questions_indices=get_random_question_index(easy_questions)
    medium_questions_indices=get_random_question_index(medium_questions)
    hard_questions_indices=get_random_question_index(hard_questions)

    all_player_questions=[]
    
    for question in easy_questions_indices:
        single_question=easy_questions[question]
        all_player_questions.append(single_question)

    for question in medium_questions_indices:
        single_question=medium_questions[question]
        all_player_questions.append(single_question)

    for question in hard_questions_indices:
        single_question=hard_questions[question]
        all_player_questions.append(single_question)

    return all_player_questions
        
def get_question(index):
    all_questions=get_questions_ready()
    question=all_questions[index]
    question_obj=Question(question)
    return question_obj
    
def print_question_with_choices(question,index):
    padding=10
    option_padding=padding*2
    print(f' '.ljust(padding)+str(index+1)+" "+question.get_question_txt().ljust(padding)+'')
    print(f''.ljust(1)+"".center(len(str(index+1)+question.get_question_txt())+option_padding,"-")+'')
    print(f''.ljust(option_padding)+'1 ) '+question.get_question_option(1).ljust(option_padding))
    print(f''.ljust(option_padding)+'2 ) '+question.get_question_option(2).ljust(option_padding))
    print(f''.ljust(option_padding)+'3 ) '+question.get_question_option(3).ljust(option_padding))
    print(f''.ljust(option_padding)+'4 ) '+question.get_question_option(4).ljust(option_padding)+'\n')



    
    
