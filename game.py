
from player import Player
import utilities
import os
from pprint import pprint





def main():
    """
    the main function of the game
    """

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
    exit = False
    while not exit:
        utilities.print_game_menu()
        game_choice=input("Your choice: \n")
        if utilities.validate_integer_input(game_choice):
            if int(game_choice)==1:
                player_details=utilities.get_player_data()
                player_obj=Player(player_details)
                players=utilities.SHEET.worksheet('player')
                players.append_row(player_obj)
                
                #starting the game
                win = False
                usr_choices=[]
                for index in range(5):
                    question=utilities.get_question(index)
                    utilities.print_question_with_choices(question,index)
                    while True:
                        usr_selection=input("Enter your choice from 1 to 4 \n")
                        if utilities.validate_integer_input(usr_selection):
                            print("it is valid input")
                            break
                        else:
                            print("it is not valid input\n")
                    
                    if question.check_usr_answer(usr_selection):
                        print("Correct \n")
                    else:
                        print("Your choice is wrong\n")
                        break
            elif int(game_choice)==2:
                utilities.show_game_instructions()
                if utilities.get_user_choice()=="e":
                    print("Finish Game")
                    exit=True
               

            elif int(game_choice)==3:
                exit = True

