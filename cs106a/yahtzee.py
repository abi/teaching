# Yahtzee in Python
# =================

# In this example, we are going to rewrite in Python the Yahtzee assignment that you completed a couple of weeks ago in Java.

# When we are done, the code for validating each Yahtzee category will, on average, be just **1** line!

# Welcome to Python!
# ==================

# Python is one of the most beautiful languages known to man.  
# Python has no `;`s at the end of lines.  
# Python has no braces (instead, indentation determines what's inside an `if` statement or `for` loop).  
# It doesn't even have that many parentheses.  
# AND It reads a lot like English!

# The Zen of Python 
# =================

# *The Zen of Python* is an official document that describes how Python the language was designed and is maintained.
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
#  * Namespaces are one honking great idea -- let's do more of those!

# If you want to see how these principles show in practice in Python, [check this out](http://stackoverflow.com/questions/228181/the-zen-of-python).

# Category constants
# ==================

# Nothing to see here really.

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

# This method is actually really short if you took out the comments.
# If you wrote the same method in Java, it would be much longer.

# As you can see, method arguments and variables in Python don't have any type annotations.
# This is really nice because it speeds up the process of writing programs a lot.

def findScore(dice, category):
    
    # Let's create an array of all the possible different faces of a die.
    # You'll see why this is useful in a minute.
    faces = [1, 2, 3, 4, 5, 6]
    
    # Now, we write a simple one-line helper method that:
    # given a face (1-6), returns the frequency/count of that face among the current set of dice.
    def getCount(face): return dice.count(face)
    # So if our `dice = [2, 3, 1, 2, 1]`, `getCount(1)` would equal `2`. Do you see why?
    
    # **`map`** is a function/method defined in Python that literally maps every element from an array
    # to a corresponding element in a new array.
    
    # It takes two arguments: (1) a method to apply on every element, and (2) the array.
    # To be clear, it doesn't modify the `faces` variable/array in any way.
    counts = map(getCount, faces)
    
    # Let's explore what `map(getCount, faces)` actually does in detail with an example:  
    # If we have the array as below:  
    #  ->  &nbsp;&nbsp;&nbsp; **[1,                   2,              3,          4,              5,                  6]**  
    # When we call `map(getCount, faces)`, it returns a new array that is filled up as follows:  
    #  -> &nbsp;&nbsp;&nbsp; [`dice.count(1)`, `dice.count(2)`, `dice.count(3)`, `dice.count(4)`, `dice.count(5)`, `dice.count(6)`]  
    # So, if our `dice` variable is:    
    # -> &nbsp;&nbsp;&nbsp; **[2, 3, 1, 2, 1]**   
    # The values we would have in the `counts` variable would be:    
    # -> &nbsp;&nbsp;&nbsp; **[2, 2, 1, 0, 0, 0]**  
    # Does that make sense? The `counts` array is going to make our life much easier when determining categories.

    # Ones, twos, threes, ...
    # ---------------------
    
    # `in` is a Python keyword that, given `a in b`, checks if `a` is a member of the array `b`.
    # So, the next line is equivalent to the Java code:
    
    # `category == 0 || category == 1 || category == 2 || ...`
    
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        # Because categories are zero-indexed, we want to add `1` to `category` and then, find the count of the result.
        # So, if we are checking the `TWOs` category, this line finds the number of dices that have `2` on them
        # (this is what `dice.count(2)` will return) and then, multiplies that by `2` to get the sum of all dice
        # that equal `2` in the current set.
        return getCount(category + 1) * (category + 1)
    
    # Three of a Kind, Four of a Kind, Yahtzee
    # ----------------------------------------
    
    elif category in [THREE_OF_A_KIND, FOUR_OF_A_KIND, YAHTZEE]:
        # Yahtzee is simply a five of kind and so, it's really similar to both three of a kind and four of a kind.
        
        # First, let's calculate `n` where `n` is the type of a kind the `category` is:
        
        # * `THREE_OF_A_KIND` is when `n = 3`
        # * `FOUR_OF_A_KIND` is when `n = 4`
        # * `YAHTZEE` is when `n = 5`
        
        # Because `THREE_OF_A_KIND` and `FOUR_OF_A_KIND` are defined to be integer constants `8`, `9` respectively,  
        # we can simply subtract `5`. Because `YAHTZEE` is `13`, we subtract `8`.
        if category is YAHTZEE:
            n = category - 8
        elif category is THREE_OF_A_KIND or category is FOUR_OF_A_KIND:
            n = category - 5
        
        for face in faces:
            # Great. Now, we have the correct `n`. Let's go through every face in faces -
            # oh, but first, I almost forgot to mention it but this is how you do for loops in Python! It's beautifully concise, isn't it?
            # This is functionally equivalent to the Java code:  

            #`for(int i=0;i<faces.length-1;i++){int face = face[i];}`

            # WOAH.
            
            # If the count of any `face` is greater than `n`, then just return the sum of all elements in an array
            # Python has a neat `sum` method that works on arrays, sets, etc.  
            
            # Take **`[1, 1, 2, 2, 2]`**  
            
            # When we are going through the `faces` array and we're at `face = 2`, 
            # we'll find its count to be `3`, and if we are looking for a `THREE_OF_A_KIND`, then this is it!  
            
            # If we're looking for a `FOUR_OF_A_KIND` or `YAHTZEE`, we pass and we just keep iterating through the array,
            # Eventually, at the end of this function, we'll return `0` because the `dice` don't match the `category`.
            if getCount(face) >= n: return sum(dice)
            # Does that all make sense?
            # We just unified all nOfAKind-type problems and solved them very simply. Awesome. Onward and upward.
            
    # Full house
    # ---------
    
    elif category is FULL_HOUSE:
        # What is a full house?
        # A full house is a set of dice where one face appears 2 times and another face appears 3 times
        # (and importantly, they can't both be the same face).
        
        # Going back to the `counts` array we created earlier, what would it look like if the dice was a valid
        # full house?
        
        # `[0, 0, 0, 0, 2, 3]` of course!
        
        # Or it could be `[0, 0, 2, 0, 0, 3]` or `[3, 0, 2, 0, 0, 0]`. How do unify all these different cases of
        # valid full houses? I mean, all of them have a `2` and a `3` exactly once. The rest of the elements in the array are `0`s.
        # There should probably be a simple way, right?
        
        # Right! One trick we could use is sorting.
        counts.sort()
        # What would any valid full house `counts` array look like now that it is sorted?
        
        # -> `[0, 0, 0, 0, 2, 3]`
        
        # Sorting basically makes `[0, 2, 3, 0, 0, 0]` and `[2, 0, 0, 0, 0, 3]` and what-have-you equivalent
        # because it puts the numbers in order. The `0`s always go first in a sorted array, then the `2`, then the `3`.
        
        if counts == [0, 0, 0, 0, 2, 3]: return 25
        # Well, that was easy.
        
    # Large straight
    # -------------
    
    elif category is LARGE_STRAIGHT:
        # Detecting a large straight isn't too hard either.
        
        # There are only two valid large straights with 5 dice: **1, 2, 3, 4, 5** and **2, 3, 4, 5, 6**.
        # So, we see that every face only appears once. 
        # What would the counts look like in either case?
        
        # `[1, 1, 1, 1, 1, 0]` or `[0, 1, 1, 1, 1, 1]`. Duh.
        
        # To solve this problem, we basically want to detect if the array `[1, 1, 1, 1, 1]` is a *sub*array of `counts`
        # Hmm... sub*array* sounds awfully similar to sub*string*, doesn't it?
        
        # Let's make `counts` into a string and
        # check for the substring `"11111"` then!
        
        countsStr = "".join(map(str, counts))
        # Because `counts` is an array of ints, we use the `str` method (which converts anything to a string) and the `map` method
        # to make it an array of strings. Then, we join all the individual characters into the `countsStr` string.
        
        # Did I mention you can just use the `in` keyword to check substrings in Python?
        if "11111" in countsStr: return 40
        
        #And that's it. Just 2 lines to detect large straights.
        
    # Small straight
    # -------------
        
    elif category is SMALL_STRAIGHT:
        # A large straight is also a small straight.
        # But a small straight doesn't have to be a large straight.
        # How do we check for it?
        # I think you can do this by yourself. It's quite elementary, my dear reader.
        countsStr = "".join(map(str, counts))
        if "11111" in countsStr or \
            "2111" in countsStr or "1211" in countsStr or "1121" in countsStr  or "1112" in countsStr:
            return 30
        
    # And finally, Chance.
    # --------------------
    elif category is CHANCE: return sum(dice)
    
    # If this function did not return inside one of the categories, that means the `dice` don't match the `category`.
    # `0` points for that.
    return 0
    


# Playing with this program
# =========================

# In order to run this program, you need to first install Python. 

# Installing Python
# -----------------

# Installing Python shouldn't take too long (probably around 10-15 mins).
# There are [detailed instructions here](http://getpython3.com/diveintopython3/installing-python.html)
# for all the popular operating systems.

# Changing the dice and category
# ------------------------------

# Now that you have Python installed, download this file and run it.
# Download links:

# * [Download with comments](https://raw.github.com/abi/teaching/master/cs106a/yahtzee.py)
# * [Download without comments](https://raw.github.com/abi/teaching/master/cs106a/yahtzee-nc.py)

# Change the dice and category that you want to check here.

dice = [2, 2, 4, 5, 6]
category = SMALL_STRAIGHT
print "The score for that category with " + str(dice) + " is " +  str(findScore(dice, category))

# Testing
# =======

def test():
    
    # Assertions are things you are telling the computer should always be true.
    # Try modifying findScore to make it somehow wrong and then, running the tests!
    # The computer will complain that your tests are failing.
    
    # Testing is a incredibly useful tool to make sure when we change some bit of code, we
    # don't unintentionally break other parts of the code. Testing also makes writing programs *much* faster.
    
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

# Think you might like Python?
# ============================

# Check out these resources (all of these are free):

# * [A Gentle Introduction to Programming Using Python](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/)
# * [How to Think Like a Computer Scientist](http://greenteapress.com/thinkpython/thinkCSpy/)
# * [Learn Python The Hard Way](http://learnpythonthehardway.org/book/)
# * [Dive Into Python](http://getpython3.com/diveintopython3/)
