from top_scores import TopScores, PlayerScore
import pytest

def test_top_scores_empty():
    top_scores = TopScores()
    assert len(top_scores) == 0


def test_top_scores_one():
    top_scores = TopScores()
    top_scores.add(player="Mark",score=200)
    assert len(top_scores) == 1
    assert top_scores.get_player(0) == "Mark"
    assert top_scores.get_score(0) == 200

def test_top_scores_three():
    top_scores = TopScores()
    top_scores.add(player="Mark",score=200)
    top_scores.add(player="Beth",score=300)
    top_scores.add(player="Phil",score=100)
    assert len(top_scores) == 3
    assert top_scores.get_player(0) == "Beth"
    assert top_scores.get_score(0) == 300
    assert top_scores.get_player(1) == "Mark"
    assert top_scores.get_score(1) == 200
    assert top_scores.get_player(2) == "Phil"
    assert top_scores.get_score(2) == 100

def test_top_scores_over_five():
    top_scores = TopScores()
    top_scores.add(player="Mark",score=200)
    top_scores.add(player="Beth",score=300)
    top_scores.add(player="Phil",score=100)
    top_scores.add(player="Second",score=250)
    top_scores.add(player="End",score=1)
    top_scores.add(player="Third",score=225)
    assert len(top_scores) == 5
    

