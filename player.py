class Player:
    """
    used to initialize the player data later on more data 
    will be saved here like birth year to get the age and the email address. 
    """
    def __init__(self, player_data):
        self.fullname = player_data[0]
        self.country = player_data[1]
        self.score = 0
    
    def get_player_details(self):
        player = []
        player.append(self.fullname)
        player.append(self.country)
        return player
    
    def get_player_with_score(self):
        player = []
        player.append(self.fullname)
        player.append(self.country)
        player.append(self.score)
        return player

    def increase_player_score(self,index):
        if index == 1:
            self.score = 100
        elif index == 5:
            self.score = 1000
        elif index == 12:
            self.score = 125000
        else:
            self.score += self.score
    
    def update_safety_score(self):
        if self.score >= 32000:
            self.score = 32000
        elif self.score >= 1000:
            self.score = 1000
        else:
            self.score
        
        return self.score
    
    def play_again(self):
        """
        reset the score of current player to zero
        """
        self.score=0