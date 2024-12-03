class Score():
    def __init__(self):
        self.points = 0
        self.goals = 0
    
    def __str__(self):
        return f"{self.goals:02d}:{self.points:02d}"
    
    def addPoint(self):
        self.points += 1

    def addGoal(self):
        self.goal += 1

    def calculateScore(self):
        return (self.points * 1) + (self.goals * 3)

myScore = Score()
print(myScore)