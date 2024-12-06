class Score():
    """
    A class representing a Score.

    Attributes:
        points (int): The number of points scored.
        goals (int): The number of points scored.
    """
    def __init__(self, points=0, goals=0):
        """
        Initializes a Score object which can be default or passed parameters.

        Parameters:
            points (int): Default:0. The number of points scored.
            goals (int): Default:0. The number of points scored.
        """
        self.points = points
        self.goals = goals
    
    def __str__(self):
        """Displays a string representation of the score object"""
        return f"{self.goals:02d}:{self.points:02d}"
    
    def addPoint(self):
        """Increments the points variable"""
        self.points += 1

    def addGoal(self):
        """Increments the goals variable"""
        self.goals += 1

    def calculateScore(self) -> int:
        """Increments the goals variable
        
        Returns: 
            int: The score of calculated as a number.
        """
        return (self.points * 1) + (self.goals * 3)

myScore = Score()
print(myScore)