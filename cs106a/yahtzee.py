# Welcome to Python!
# ==================

# Python is one of the most beautiful languages known to man.
# Python has no ';'s at the end of lines.
# Python has no braces (instead, indentation determines what's inside an if statement or for loop).
# Not even that many parentheses!
# AND It reads a lot like English!

# The Zen of Python 
# =================

# The Zen of Python is an official document that describes how Python the language was designed and is maintained.
# The beauty of the language no doubt derives from these principles. They are also pretty amusing:

#  * Beautiful is better than ugly.
#  * Explicit is better than implicit.
#  * Simple is better than complex.
#  * Complex is better than complicated.
#  * Flat is better than nested.
#  * Sparse is better than dense.
#  * Readability counts.
#  * Special cases aren't special enough to break the rules.
#  * Although practicality beats purity.
#  * Errors should never pass silently.
#  * Unless explicitly silenced.
#  * In the face of ambiguity, refuse the temptation to guess.
#  * There should be one-- and preferably only one --obvious way to do it.
#  * Although that way may not be obvious at first unless you're Dutch.
#  * Now is better than never.
#  * Although never is often better than *right* now.
#  * If the implementation is hard to explain, it's a bad idea.
#  * If the implementation is easy to explain, it may be a good idea.


# Category constants
# ==================

# Nothing to see here really

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

# The Meat 
# ==========

# This method is actually really short if not for the comments.
# If you wrote the same method in Java, it would be much longer.
# As you can see method arguments and variables in Python don't have any type annotations
# This is really nice because it speeds up the process of programming a lot.

def findScore(dice, category):
    
    # Let's create an array of all the possible different faces of a die
    # You'll see why this is useful in a minute
    faces = [1, 2, 3, 4, 5, 6]
    
    # We write a simple one-line helper method that:
    #       Given a face (1-6), returns the frequency/count of that face among the current set of dice
    def getCount(face): return dice.count(face)
    # So if our dice = [2, 3, 1, 2, 1], getCount(1) would equal 2
    
    # Map is a function/method defined in Python that literally maps from one element from an array
    # to a different element in a new array
    # It takes two arguments: (1) a method to apply on every element, and (2) the array
    # To be clear, it doesn't modify faces in any way
    counts = map(getCount, faces)
    
    # Let's explore what this actually does in detail with an example:
    # If we have the array as below:
    #  ->  [1,                   2,              3,          4,              5,                  6]
    # When we call `map(getCount, faces)`, it retun a new array that is filled up as follows
    #  -> [dice.count(1), dice.count(2), dice.count(3), dice.count(4), dice.count(5), dice.count(6)]
    # So, if our dice = [2, 3, 1, 2, 1],
    # The values we would have would be
    # -> [2, 2, 1, 0, 0, 0]
    # Do you see why?
    
    # Now, let's sort the counts array
    # Don't worry about why we do this, we'll get back to it
    counts.sort()
    # What would the example counts array look like now?
    # -> [0, 0, 0, 1, 2, 2]

    # `in` is a keyword that checks, given a `in` b, checks if a is a member of the array b.
    # So, the next line is equivalent to the Java code: category == 0 || category == 1 || category == 2 || ...
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        # Because categories are zero-indexed, we want to add 1 to it and then, find the count of the result
        # So, if we are checking the TWOs category, the line below finds the number of dices that have 2 on them
        # (this is what dice.count(2) will return) and then, multiplies that by 2 to get the sum of all dice
        # that equal 2 in the current set
        return dice.count(category + 1) * (category + 1) 
    elif category in [THREE_OF_A_KIND, FOUR_OF_A_KIND, YAHTZEE]:
        # First, let's calculate n where n is type ofAKind something is
        # 3ofAKind is when n = 3
        # 4ofAKind is when n = 4
        # 5ofAKind is when n = 5
        if category is YAHTZEE:
            n = category - 8
        elif category is THREE_OF_A_KIND or category is FOUR_OF_A_KIND:
            n = category - 5    
        
        # Let's go through every face in faces - 
        # Oh, actually, but first, this is how you do for loops in Python! It's beautifully concise, isn't it?
        # This is functionally equivalent to the Java code: `for(int i=0;i<faces.length-1;i++){int face = face[i];}`
        # WOAH
        for face in faces:
            # If the count of any face is greater than n, then just return the sum of all elements in an array
            # Python has a neat sum() method that works on arrays, sets, etc.
            # Take [1, 1, 2, 2, 2],
            # When we are going through the `faces` array and we're at face = 2
            # We'll find its count to be 3, and if we are looking for a three of a kind, then this is it!
            # If we're looking for a four of kind, we pass and we just keep iterating through the array
            # Eventually, at the end of this function, we'll return zero
            if dice.count(face) >= n: return sum(dice)
            # Does that make sense?
            # We unified all nOfAKind-type problems and solved them very simply. Awesome. Onward and upward.
    elif category is FULL_HOUSE:
        # What is a full house?
        # A full house is a set of dice, where one face appears 2 times and another face appears 3 times
        # (and importantly, they can't both be the same face)
        # Going back to the counts array we created earlier, what would it look like if the dice was a valid
        # full house?
        # [0, 0, 0, 0, 2, 3] of course!
        # Can it look any other way if it's a valid full house? Nope.
        # And this is also why we sorted counts. Sorting basically makes [0, 2, 3, 0, 0, 0] and [2, 0, 0, 0, 0, 3]
        # equivalent.
        # Well, that was easy
        if counts == [0, 0, 0, 0, 2, 3]: return 25
    # TODO, Fix bugs
    elif category is LARGE_STRAIGHT:
        # Large straight is just as easy
        # There are only two valid large straights with 5 dice: 1, 2, 3, 4, 5 or 2, 3, 4, 5, 6
        # So, we see that every face only appears once. 
        # What would the counts look like in either case?
        # [0, 1, 1, 1, 1, 1] Duh.
        if counts == [0, 1, 1, 1, 1, 1]: return 40
    elif category is SMALL_STRAIGHT:
        # A large straight is also a small straight
        # But a small straight doesn't have to be a large straight
        # How do we check for it?
        # You can figure it out. It's pretty easy.
        if counts in [[0, 0, 1, 1, 1, 2], [0, 1, 1, 1, 1, 1]]:return 30
    elif category is CHANCE: return sum(dice)
    
    # If it did not return inside one of the categories, that means the dice don't match the category
    # 0 points for that
    return 0
    


# Playing with this program
# =========================


# CHANGE the dice and category that you want to check here
dice = [2, 2, 4, 5, 6]
category = SMALL_STRAIGHT
print "The score for that category with " + str(dice) + " is " +  str(findScore(dice, category))

# Testing
# =======

def test():
    # Assertions are things you are telling the computer should be true
    # Try modifying findScore to make it somehow wrong and then, running the tests!
    # The computer will complain that your tests are failing.
    # Testing is a incredibly useful tool to make sure when we change some bit of code, we
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
    assert findScore([5, 2, 2, 4, 5], SMALL_STRAIGHT) is 0
    assert findScore([5, 2, 2, 2, 5], SMALL_STRAIGHT) is 0
    assert findScore([1, 5, 5, 5, 5], CHANCE) is 21
    assert findScore([5, 5, 5, 5, 5], CHANCE) is 25
    print "Successfully ran ALL tests!"

test()