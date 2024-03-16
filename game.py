import gspread
from google.oauth2.service_account import Credentials
import game


from player import Player




SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('who_wants_to_be_a_millionair')

"""
following lines are just for testing the connection
"""
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

 

def main():
    """
    the main function of the game
    """
    print_game_title()
    player_details=get_player_data()
    player_obj=Player(player_details)
    players=SHEET.worksheet('player')
    players.append_row(player_obj)

    

