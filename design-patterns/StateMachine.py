# StateMachine/State.py
# A State has an operation, and can be moved
# into the next State given an Input:

class State:
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"

# StateMachine/StateMachine.py
# Takes a list of Inputs to move from State to
# State using a template method.

class StateMachine:
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.run()
    # Template method:
    def runAll(self, inputs):
        for i in inputs:
            print(i)
            self.currentState = self.currentState.next(i)
            self.currentState.run()

# StateMachine/mouse/MouseAction.py

class MouseAction:
    def __init__(self, action):
        self.action = action
    def __str__(self): return self.action
    def __cmp__(self, other):
        return cmp(self.action, other.action)
    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:
    def __hash__(self):
        return hash(self.action)

# Static fields; an enumeration of instances:
MouseAction.appears = MouseAction("mouse appears")
MouseAction.runsAway = MouseAction("mouse runs away")
MouseAction.enters = MouseAction("mouse enters trap")
MouseAction.escapes = MouseAction("mouse escapes")
MouseAction.trapped = MouseAction("mouse trapped")
MouseAction.removed = MouseAction("mouse removed")

# StateMachine/mousetrap1/MouseTrapTest.py
# State Machine pattern using 'if' statements
# to determine the next state.
import string, sys
sys.path += ['../stateMachine', '../mouse']

#from State import State
#from StateMachine import StateMachine
#from MouseAction import MouseAction

# A different subclass for each state:

class Waiting(State):
    def run(self):
        print("Waiting: Broadcasting cheese smell")

    def next(self, input):
        if input == MouseAction.appears:
            return MouseTrap.luring
        return MouseTrap.waiting

class Luring(State):
    def run(self):
        print("Luring: Presenting Cheese, door open")

    def next(self, input):
        if input == MouseAction.runsAway:
            return MouseTrap.waiting
        if input == MouseAction.enters:
            return MouseTrap.trapping
        return MouseTrap.luring

class Trapping(State):
    def run(self):
        print("Trapping: Closing door")

    def next(self, input):
        if input == MouseAction.escapes:
            return MouseTrap.waiting
        if input == MouseAction.trapped:
            return MouseTrap.holding
        return MouseTrap.trapping

class Holding(State):
    def run(self):
        print("Holding: Mouse caught")

    def next(self, input):
        if input == MouseAction.removed:
            return MouseTrap.waiting
        return MouseTrap.holding

class MouseTrap(StateMachine):
    def __init__(self):
        # Initial state
        StateMachine.__init__(self, MouseTrap.waiting)

# Static variable initialization:
MouseTrap.waiting = Waiting()
MouseTrap.luring = Luring()
MouseTrap.trapping = Trapping()
MouseTrap.holding = Holding()

moves = map(string.strip,
  open("../mouse/MouseMoves.txt").readlines())
MouseTrap().runAll(map(MouseAction, moves))
