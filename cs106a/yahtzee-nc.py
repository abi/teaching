ONES = 0
TWOS = 1
THREES = 2
FOURS = 3
FIVES = 4
SIXES = 5
UPPER_SCORE = 6
UPPER_BONUS = 7
THREE_OF_A_KIND = 8
FOUR_OF_A_KIND = 9
FULL_HOUSE = 10
SMALL_STRAIGHT = 11
LARGE_STRAIGHT = 12
YAHTZEE = 13
CHANCE = 14
LOWER_SCORE = 15
TOTAL = 16
def findScore(dice, category):
    faces = [1, 2, 3, 4, 5, 6]
    def getCount(face): return dice.count(face)
    counts = map(getCount, faces)
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return getCount(category + 1) * (category + 1)
    elif category in [THREE_OF_A_KIND, FOUR_OF_A_KIND, YAHTZEE]:
        if category is YAHTZEE:
            n = category - 8
        elif category is THREE_OF_A_KIND or category is FOUR_OF_A_KIND:
            n = category - 5
        for face in faces:
            if getCount(face) >= n: return sum(dice)
    elif category is FULL_HOUSE:
        counts.sort()
        if counts == [0, 0, 0, 0, 2, 3]: return 25
    elif category is LARGE_STRAIGHT:
        countsStr = "".join(map(str, counts))
        if "11111" in countsStr: return 40
    elif category is SMALL_STRAIGHT:
        countsStr = "".join(map(str, counts))
        if "11111" in countsStr or \
            "2111" in countsStr or "1211" in countsStr or "1121" in countsStr  or "1112" in countsStr:
            return 30
    elif category is CHANCE: return sum(dice)
    return 0
dice = [2, 2, 4, 5, 6]
category = SMALL_STRAIGHT
print "The score for that category with " + str(dice) + " is " +  str(findScore(dice, category))
def test():
    assert findScore([1, 1, 5, 5, 5], ONES) is 2
    assert findScore([1, 1, 5, 5, 5], FIVES) is 15
    assert findScore([1, 1, 5, 5, 5], THREE_OF_A_KIND) is 17
    assert findScore([1, 1, 5, 5, 5], FOUR_OF_A_KIND) is 0
    assert findScore([1, 5, 5, 5, 5], FOUR_OF_A_KIND) is 21
    assert findScore([6, 6, 6, 6, 6], YAHTZEE) is 30
    assert findScore([1, 1, 5, 5, 5], FULL_HOUSE) is 25
    assert findScore([2, 2, 3, 5, 5], FULL_HOUSE) is 0
    assert findScore([1, 2, 3, 4, 5], LARGE_STRAIGHT) is 40
    assert findScore([1, 2, 3, 4, 5], SMALL_STRAIGHT) is 30
    assert findScore([2, 2, 3, 4, 5], SMALL_STRAIGHT) is 30
    assert findScore([1, 2, 3, 4, 5], SMALL_STRAIGHT) is 30
    assert findScore([5, 2, 2, 4, 5], SMALL_STRAIGHT) is 0
    assert findScore([2, 2, 3, 5, 6], SMALL_STRAIGHT) is 0
    assert findScore([5, 2, 2, 2, 5], SMALL_STRAIGHT) is 0
    assert findScore([1, 5, 5, 5, 5], CHANCE) is 21
    assert findScore([5, 5, 5, 5, 5], CHANCE) is 25
    print "Successfully ran ALL tests!"
test()
