

class ScoreBoard:
    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2
        self.score_team1 = 0;
        self.score_team2 = 0;

    def update(self):
        self.scroe_team1 = 0
        self.score_team2 = 0
        for unit in self.team1:
            self.score_team1 += self.team1[unit].kill
        for unit in self.team2:
            self.score_team2 += self.team2[unit].kill

    def get_score(self,team = 1):
        if team == 1:
            return self.score_team1
        elif team == 2:
            return self.score_team2
        else:
            print("has not team")
