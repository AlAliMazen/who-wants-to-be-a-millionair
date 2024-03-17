import gspread
from google.oauth2.service_account import Credentials
import random

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
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n")
    print("|      WHO WANTS TO BE A MILLIONAIRE          |\n")
    print("|_____________________________________________|\n\n")

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

def update_questions_worksheet(question_level, questions_list):
    questions=SHEET.worksheet(question_level)
    data=questions.get_all_values()
    if len(data)==1:
        print(f'update{question_level} worksheet ...\n')
        questions.append_rows(questions_list)
        print(f'{question_level} worksheet was updated successfully\n')
    else:
        print(f'{question_level} worksheet has already populated with questions\n')


def get_random_question_index(question_list):
    """
    get a random index which represents the question row starting at one to 
    exclude the headings till the last question
    """
    return random.random(1,len(question_list))