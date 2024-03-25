
from player import Player
import utilities
from pprint import pprint
import time
import utilities

def get_player_info():
    player_details=utilities.get_player_data()
    player_obj = Player(player_details)
    players = utilities.SHEET.worksheet('player')
    players.append_row(player_obj.get_player_details())
    utilities.clear_console()
    return player_obj

def start_game(player_obj):
    questions = utilities.get_questions_ready()
    for index in range(15):
        utilities.print_player_info(player_obj.get_player_with_score(), index+1)
        utilities.print_game_title()
        question=utilities.get_question( questions[index])
        utilities.print_question_with_choices(question, index)
        while True:
            usr_selection=input("Enter your choice from 1 to 4 \n")
            if not utilities.validate_integer_input(usr_selection.strip()):
                print("Invalid option\n")
            else:
                break

        if question.check_usr_answer(usr_selection.strip()):
            print("Correct \n")
            player_obj.increase_player_score(index+1)
            time.sleep(3)
            utilities.clear_console()
            if index+1 == 15:
                player_obj.update_safety_score()
                utilities.print_winner_info(player_obj.get_player_with_score(), index+1)
                break
        else:
            print("\n\nYour choice is wrong\n Game Over!\n")
            player_obj.update_safety_score()
            utilities.update_scoring_sheet(player_obj.get_player_with_score(), index+1)
            time.sleep(3)
            utilities.clear_console()
            utilities.print_player_info(player_obj.get_player_with_score(), index)
            break
            


def main():
    """
    the main function of the game
    """
    utilities.read_questions_txt_files()
    utilities.clear_console()
    exit = False
    while not exit:
        utilities.print_game_menu()
        game_choice=input("Your choice: \n")
        if utilities.validate_integer_input(game_choice):
            if int(game_choice) == 1:
                player_obj=get_player_info()
                start_game(player_obj)
                play_again = utilities.play_again_mechanism(player_obj)
                if play_again:
                    utilities.clear_console()
                    start_game(player_obj)                    
                else:
                    utilities.end_game_message()
                    exit = True
            elif int(game_choice) == 2:
                utilities.show_game_instructions()
                if utilities.get_user_choice() == "e":
                    utilities.end_game_message()
                    exit=True
            elif int(game_choice)==3:
                utilities.get_scoring_board()
                if utilities.get_user_choice() == "e":
                    utilities.end_game_message()
                    exit=True
            elif int(game_choice)==4:
                utilities.end_game_message()
                exit = True

