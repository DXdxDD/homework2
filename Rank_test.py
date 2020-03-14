import unittest
import Rank
def testScore9():
    temp = Rank.Card(["2D", "3D", "4D", "5D", "6D"])
    score = temp.getScore()
    assert score == 9
def testScore8():
    temp = Rank.Card(["2D", "2H", "2C", "2S", "6D"])
    score = temp.getScore()
    assert score == 8
def testScore7():
    temp = Rank.Card(["2D", "2H", "2C", "5D", "5C"])
    score = temp.getScore()
    assert score == 7
def testScore6():
    temp = Rank.Card(["2D", "3D", "7D", "5D", "6D"])
    score = temp.getScore()
    assert score == 6
def testScore5():
    temp = Rank.Card(["2D", "3D", "4S", "5D", "6D"])
    score = temp.getScore()
    assert score == 5
def testScore4():
    temp = Rank.Card(["2D", "2C", "2H", "5D", "6D"])
    score = temp.getScore()
    assert score == 4
def testScore3():
    temp = Rank.Card(["2D", "2H", "4D", "4H", "6D"])
    score = temp.getScore()
    assert score == 3
def testScore2():
    temp = Rank.Card(["2D", "3D", "3S", "4H", "8S"])
    score = temp.getScore()
    assert score == 2
def testScore1():
    temp = Rank.Card(["2D", "7H", "4D", "5D", "6D"])
    score = temp.getScore()
    assert score == 1
def testcompBlack():
    black = Rank.Card(["2D", "3D", "4D", "5D", "6D"])
    white = Rank.Card(["2D", "3D", "3S", "4H", "8S"])
    str = Rank.comp(black, white)
    assert str == "black"
def testcompBlack():
    black = Rank.Card(["2D", "3D", "3S", "4H", "8S"])
    white = Rank.Card(["2D", "3D", "4D", "5D", "6D"])
    str = Rank.comp(black, white)
    assert str == "white"
def testcompBlack():
    black = Rank.Card(["2D", "3D", "4D", "5D", "6D"])
    white = Rank.Card(["2D", "3D", "4D", "5D", "6D"])
    str = Rank.comp(black, white)
    assert str == "pingju"
