from pprint import pprint
class Question:
    """
    every question is going to be gathered in a set to guantee that 
    it has no duplicates
    """
    def __init__(self, question):
        self.question=question[0]
        self.opt_a=question[1]
        self.opt_b=question[2]
        self.opt_c=question[3]
        self.opt_d=question[4]
        self.r_index=question[5]

    
    
    def check_usr_answer(self, usr_answer):
        """
        chick user answer whether it is the same as the question real answer
        """
        return True if self.r_index==usr_answer else False
    

    def get_question_txt(self):
        """
        get question text
        """
        return self.question

    def get_question_option(self, option):
        if option==1:
            return self.opt_a
        elif option==2:
            return self.opt_b
        elif option==3:
            return self.opt_c
        elif option==4:
            return self.opt_d
    