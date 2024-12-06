import pytest
import Game
def test_that_passes():
    assert True

def test_score_default_init():
    score = Game.Score()
    assert score.points == 0 and score.goals == 0

def test_score_init():
    score = Game.Score(11,5)
    assert score.points == 11 and score.goals == 5

def test_score_points():
    score = Game.Score()
    score.addPoint()
    assert score.points == 1 and score.goals == 0

def test_score_goals():
    score = Game.Score()
    score.addGoal()
    assert score.points == 0 and score.goals == 1

def test_score_to_string():
    score = Game.Score()
    assert f"{score}" == "00:00"