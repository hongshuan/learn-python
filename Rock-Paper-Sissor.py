# MultipleDispatching/PaperScissorsRock.py
# Demonstration of multiple dispatching.
from __future__ import generators
import random

# An enumeration type:
class Outcome:
    def __init__(self, value, name):
        self.value = value
        self.name = name
    def __str__(self): return self.name
    def __eq__(self, other):
        return self.value == other.value

Outcome.WIN = Outcome(0, "win")
Outcome.LOSE = Outcome(1, "lose")
Outcome.DRAW = Outcome(2, "draw")

class Item(object):
    def __str__(self):
        return self.__class__.__name__

class Paper(Item):
    def compete(self, item):
        # First dispatch: self was Paper
        return item.evalPaper(self)
    def evalPaper(self, item):
        # Item was Paper, we're in Paper
        return Outcome.DRAW
    def evalScissors(self, item):
        # Item was Scissors, we're in Paper
        return Outcome.WIN
    def evalRock(self, item):
        # Item was Rock, we're in Paper
        return Outcome.LOSE

class Scissors(Item):
    def compete(self, item):
        # First dispatch: self was Scissors
        return item.evalScissors(self)
    def evalPaper(self, item):
        # Item was Paper, we're in Scissors
        return Outcome.LOSE
    def evalScissors(self, item):
        # Item was Scissors, we're in Scissors
        return Outcome.DRAW
    def evalRock(self, item):
        # Item was Rock, we're in Scissors
        return Outcome.WIN

class Rock(Item):
    def compete(self, item):
        # First dispatch: self was Rock
        return item.evalRock(self)
    def evalPaper(self, item):
        # Item was Paper, we're in Rock
        return Outcome.WIN
    def evalScissors(self, item):
        # Item was Scissors, we're in Rock
        return Outcome.LOSE
    def evalRock(self, item):
        # Item was Rock, we're in Rock
        return Outcome.DRAW

def match(item1, item2):
    print("%s <--> %s : %s" % (
      item1, item2, item1.compete(item2)))

# Generate the items:
def itemPairGen(n):
    # Create a list of instances of all Items:
    Items = Item.__subclasses__()
    for i in range(n):
        yield (random.choice(Items)(),
               random.choice(Items)())

for item1, item2 in itemPairGen(20):
    match(item1, item2)

#This was a fairly literal translation from the Java version, and one of the
#things you might notice is that the information about the various combinations
#is encoded into each type of Item. It actually ends up being a kind of table,
#except that it is spread out through all the classes. This is not very easy to
#maintain if you ever expect to modify the behavior or to add a new Item class.
#Instead, it can be more sensible to make the table explicit, like this:
'''
# MultipleDispatching/PaperScissorsRock2.py
# Multiple dispatching using a table
from __future__ import generators
import random

class Outcome:
    def __init__(self, value, name):
        self.value = value
        self.name = name
    def __str__(self): return self.name
    def __eq__(self, other):
        return self.value == other.value

Outcome.WIN = Outcome(0, "win")
Outcome.LOSE = Outcome(1, "lose")
Outcome.DRAW = Outcome(2, "draw")

class Item(object):
    def compete(self, item):
        # Use a tuple for table lookup:
        return outcome[self.__class__, item.__class__]
    def __str__(self):
        return self.__class__.__name__

class Paper(Item): pass
class Scissors(Item): pass
class Rock(Item): pass

outcome = {
  (Paper, Rock): Outcome.WIN,
  (Paper, Scissors): Outcome.LOSE,
  (Paper, Paper): Outcome.DRAW,
  (Scissors, Paper): Outcome.WIN,
  (Scissors, Rock): Outcome.LOSE,
  (Scissors, Scissors): Outcome.DRAW,
  (Rock, Scissors): Outcome.WIN,
  (Rock, Paper): Outcome.LOSE,
  (Rock, Rock): Outcome.DRAW,
}

def match(item1, item2):
    print("%s <--> %s : %s" % (
      item1, item2, item1.compete(item2)))

# Generate the items:
def itemPairGen(n):
    # Create a list of instances of all Items:
    Items = Item.__subclasses__()
    for i in range(n):
        yield (random.choice(Items)(),
               random.choice(Items)())

for item1, item2 in itemPairGen(20):
    match(item1, item2)

'''
