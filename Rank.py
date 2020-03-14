def isSameFL(temp):
    temp.tonum()
    if (temp.flower[0] == temp.flower[1] == temp.flower[2] == temp.flower[3] == temp.flower[4]):
        return True
    return False
def isSeq(temp):
    temp.tonum()
    temp.num.sort()
    if ((temp.num[0] == temp.num[1] - 1) & (temp.num[1] == temp.num[2] - 1)
    & (temp.num[2] == temp.num[3] - 1) & (temp.num[3] == temp.num[4] - 1)):
        return True
    return False
def isSame4(temp):
    temp.tonum()
    temp.num.sort()
    if ((temp.num[0] == temp.num[1] == temp.num[2] == temp.num[3])
    | (temp.num[1] == temp.num[2] == temp.num[3] == temp.num[4])):
        return True
    return False
def isHulu(temp):
    temp.tonum()
    temp.num.sort()
    if (((temp.num[0] == temp.num[1] == temp.num[2]) & (temp.num[3] == temp.num[4]))
    | ((temp.num[4] == temp.num[2] == temp.num[3]) & (temp.num[0] == temp.num[1]))):
        return True
    return False
def isSame3(temp):
    temp.tonum()
    temp.num.sort()
    if ((temp.num[0] == temp.num[1] == temp.num[2])
    | (temp.num[1] == temp.num[2] == temp.num[3]) | (temp.num[2] == temp.num[3] == temp.num[4])):
        return True
    return False
def isDouble2(temp):
    temp.tonum()
    temp.num.sort()
    if (((temp.num[0] == temp.num[1])&(temp.num[3]== temp.num[2]))
    | ((temp.num[0] == temp.num[1])&(temp.num[3]== temp.num[4]))
    | ((temp.num[2] == temp.num[1])&(temp.num[3]== temp.num[4]))):
        return True
    return False
def isDouble(temp):
    temp.tonum()
    temp.num.sort()
    if ((temp.num[0] == temp.num[1])|(temp.num[1]== temp.num[2])
    | (temp.num[2] == temp.num[3])&(temp.num[3]== temp.num[4])):
        return True
    return False
def same4_comp(black, white):
    if (black.num[0] == black.num[1] == black.num[2] == black.num[3]):
        value_b = black.num[0]
    else:
        value_b = black.num[4]
    if (white.num[0] == white.num[1] == white.num[2] == white.num[3]):
        value_w = white.num[0]
    else:
        value_w = white.num[4]
    if (value_b > value_w):
        res = 1
    else:
        res = 2
    return res
def same3_comp(black, white):
    if (black.num[0] == black.num[1] == black.num[2]):
        value_b = black.num[0]
    elif (black.num[1] == black.num[2] == black.num[3]):
        value_b = black.num[1]
    else:
        value_b = black.num[4]
    if (white.num[0] == white.num[1] == white.num[2]):
        value_w = white.num[0]
    elif (white.num[1] == white.num[2] == white.num[3]):
        value_w = white.num[1]
    else:
        value_w = white.num[4]
    if (value_b > value_w):
        res = 1
    else:
        res = 2
    return res
def dou2_comp(black, white):
    res = 0
    if ((black.num[0] == black.num[1]) & (black.num[3] == black.num[2])):
        a_b = black.num[0]
        b_b = black.num[2]
        c_b = black.num[4]
    elif ((black.num[0] == black.num[1]) & (black.num[3] == black.num[4])):
        a_b = black.num[0]
        b_b = black.num[3]
        c_b = black.num[2]
    elif ((black.num[2] == black.num[1]) & (black.num[3] == black.num[4])):
        a_b = black.num[1]
        b_b = black.num[3]
        c_b = black.num[0]
    if ((white.num[0] == white.num[1]) & (white.num[3] == white.num[2])):
        a_w = white.num[0]
        b_w = white.num[2]
        c_w = white.num[4]
    elif ((white.num[0] == white.num[1]) & (white.num[3] == white.num[4])):
        a_w = white.num[0]
        b_w = white.num[3]
        c_w = white.num[2]
    elif ((white.num[2] == white.num[1]) & (white.num[3] == white.num[4])):
        a_w = white.num[1]
        b_w = white.num[3]
        c_w = white.num[0]
    if (b_b > b_w):
        res = 1
    elif (b_b < b_w):
        res = 2
    elif (a_b > a_w):
        res = 1
    elif (a_b < a_w):
        res = 2
    elif (c_b > c_w):
        res = 1
    elif (c_b < c_w):
        res = 2
    return res
def dou1_comp(black, white):
    res = 0
    if (black.num[0] == black.num[1]):
        value_b = black.num[0]
        a_b = black.num[2]
        b_b = black.num[3]
        c_b = black.num[4]
    elif (black.num[1] == black.num[2]):
        value_b = black.num[1]
        a_b = black.num[0]
        b_b = black.num[3]
        c_b = black.num[4]
    elif (black.num[2] == black.num[3]):
        value_b = black.num[2]
        a_b = black.num[0]
        b_b = black.num[1]
        c_b = black.num[4]
    elif (black.num[3] == black.num[4]):
        value_b = black.num[3]
        a_b = black.num[0]
        b_b = black.num[1]
        c_b = black.num[2]
    if (white.num[0] == white.num[1]):
        value_w = white.num[0]
        a_w = white.num[2]
        b_w = white.num[3]
        c_w = white.num[4]
    elif (white.num[1] == white.num[2]):
        value_w = white.num[1]
        a_w = white.num[0]
        b_w = white.num[3]
        c_w = white.num[4]
    elif (white.num[2] == white.num[3]):
        value_w = white.num[2]
        a_w = white.num[0]
        b_w = white.num[1]
        c_w = white.num[4]
    elif (white.num[3] == white.num[4]):
        value_w = white.num[3]
        a_w = white.num[0]
        b_w = white.num[1]
        c_w = white.num[2]
    if (value_b > value_w):
        res = 1
    elif (value_b < value_w):
        res = 2
    else:
        if( c_b > c_w):
            res = 1
        elif( c_b < c_w):
            res = 2
        elif (b_b > b_w):
            res = 1
        elif (b_b < b_w):
            res = 2
        elif (a_b > a_w):
            res = 1
        elif (a_b < a_w):
            res = 2
    return res
def max_comp(black, white):
    res = 0
    if (black.num[4] > white.num[4]):
        res = 1
    elif (black.num[4] < white.num[4]):
        res = 2
    return res
def base_comp(black, white):
    res = 0
    for i in range(5):
        if (black .num[4-i] > white.num[4-i]):
            res = 1
            break
        elif (black .num[4-i] < white.num[4-i]):
            res = 2
            break
    return res
def comp(black, white):
    score_b = black.getScore()
    score_w = white.getScore()
    if (score_b > score_w):
        res = 1
    elif (score_b < score_w):
        res = 2
    elif ((score_b == score_w == 1) | (score_b == score_w == 6)):
        res = base_comp(black, white)
    elif ((score_b == score_w == 9) | (score_b == score_w == 5)):
        res = max_comp(black, white)
    elif (score_b == score_w == 8):
        res = same4_comp(black, white)
    elif ((score_b == score_w == 7) |(score_b == score_w == 4)):
        res = same3_comp(black, white)
    elif (score_b == score_w == 2):
        res = dou1_comp(black, white)
    elif (score_b == score_w == 3):
        res = dou2_comp(black, white)
    if res == 0:
        print("pingju")
        str = "pingju"
        return str
    elif res == 1:
        print("black")
        str = "black"
        return str
    elif res == 2:
        print("white")
        str = "white"
        return str
class Card:
    def __init__(self, cards):
        self.cards = cards

    def tonum(self):
        numlist = []
        flowerlist = []
        for str in self.cards:
            if str[0] == '2':
                num = 3
            elif str[0] == '3':
                num = 4
            elif str[0] == '4':
                num = 5
            elif str[0] == '5':
                num = 6
            elif str[0] == '6':
                num = 7
            elif str[0] == '7':
                num = 8
            elif str[0] == '8':
                num = 9
            elif str[0] == '9':
                num = 10
            elif str[0] == 'T':
                num = 11
            elif str[0] == 'J':
                num = 12
            elif str[0] == 'Q':
                num = 13
            elif str[0] == 'K':
                num = 14
            else:
                num = 15
            if str[1] == 'H':
                fl = 1
            elif str[1] == 'S':
                fl = 2
            elif str[0] == 'D':
                fl = 3
            else:
                fl = 4
            numlist.append(num)
            flowerlist.append(fl)
        self.num = numlist
        self.flower = flowerlist

    def getScore(self):
        score = 1
        if isSeq(self) & isSameFL(self):
            score = 9
        elif isSame4(self):
            score = 8
        elif isHulu(self):
            score = 7
        elif isSameFL(self):
            score = 6
        elif isSeq(self):
            score = 5
        elif isSame3(self):
            score = 4
        elif isDouble2(self):
            score = 3
        elif isDouble(self):
            score = 2
        return score
if __name__ == "__main__":
    black = Card(["8H","9D","3C","4S","AH"])
    white = Card(["8H","9D","2C","6S","7H"])
    comp(black, white)