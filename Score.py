class Score():
    def __init__(self):
        self.points = 0
        self.goals = 0
    
    def __str__(self):
        return f"{self.goals:02d}:{self.points:02d}"

myScore = Score()
print(myScore)