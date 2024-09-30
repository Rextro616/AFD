class AFD:
    def __init__(self, states, alphabet, transitions, startState, acceptStates):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.startState = startState
        self.acceptStates = acceptStates
        self.currentState = startState

    def transition(self, char):
        if (self.currentState, char) in self.transitions:
            self.currentState = self.transitions[(self.currentState, char)]
        else:
            self.currentState = None

    def isAccepting(self):
        return self.currentState in self.acceptStates

    def reset(self):
        self.currentState = self.startState

    def run(self, inputString):
        self.reset()
        for char in inputString:
            self.transition(char)
            if self.currentState is None:
                break
        return self.isAccepting()