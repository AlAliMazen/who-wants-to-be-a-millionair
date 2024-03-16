class Player:
    """
    used to initialize the player data later on more data 
    will be saved here like birth year to get the age and the email address. 
    """
    def __init__(self, player_data):
        self.fullname=player_data[0]
        self.country=player_data[1]
    
    def get_player_details(self):
        player=[]
        player.append(self.fullname)
        player.append(self.country)
        return player
    
    
