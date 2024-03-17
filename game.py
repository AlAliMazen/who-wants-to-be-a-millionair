
from player import Player
import utilities
import os
from pprint import pprint





def main():
    """
    the main function of the game
    """
    utilities.print_game_title()
    """ current_directory = os.getcwd()
    easy_questions=current_directory+"/easy-questions.txt"
    easy_questions=utilities.read_file(easy_questions)
    utilities.update_questions_worksheet("easy_questions",easy_questions)
    
    medium_questions=current_directory+"/medium-questions.txt"
    medium_questions=utilities.read_file(medium_questions)
    utilities.update_questions_worksheet("medium_questions",medium_questions)

    hard_questions=current_directory+"/hard-questions.txt"
    hard_questions=utilities.read_file(hard_questions)
    utilities.update_questions_worksheet("hard_questions",hard_questions) """
    
    #player_details=get_player_data()
    #player_obj=Player(player_details)
    #players=SHEET.worksheet('player')
    #players.append_row(player_obj)
    
    #starting the game
    win = False
    usr_choices=[]
    for index in range(15):
        question=utilities.get_question(index)
        print(type(question))
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n")
        print(f"{index+1}|{question.get_question_txt()}          |\n")
        print("|_____________________________________________|\n")
        print(f'1){question.get_question_option(1)}')
        print(f'2){question.get_question_option(2)}')
        print(f'3){question.get_question_option(3)}')
        print(f'4){question.get_question_option(4)}')

        usr_selection=input("Your option\n")
        print(f'usr choice{usr_selection}')
        usr_choices.append(usr_selection)

    pprint(usr_choices)

    

