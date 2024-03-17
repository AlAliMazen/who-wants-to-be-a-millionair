class Question:
    """
    every question is going to be gathered in a set to guantee that 
    it has no duplicates
    """
    selected_question={}
    def __init__(self, question,opt_a,opt_b,opt_c,opt_d,r_index):
        self.question=question
        self.opt_a=opt_a
        self.opt_b=opt_b
        self.opt_c=opt_c
        self.opt_d=opt_d
        self.r_index=r_index
        Question.selected_question.add(self)
    
    
    def check_usr_answer(self, usr_answer):
        """
        chick user answer whether it is the same as the question real answer
        """
        return True if self.r_index==usr_answer else False
    
    