# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os


def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def read_file(file):
    content=[]
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            content.append(line.strip())  # Stripping '\n' character from each line
        
        questions=split_list(content,5)
        return questions


    
    return questions

import game

# starting the game
#game.main()
current_path = os.getcwd()
current_path+="/easy-questions.txt"
print("Current working directory:", current_path)
print(read_file(current_path))
