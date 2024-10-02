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
            self.currentState = self.reset()

    def isAccepting(self):
        return self.currentState in self.acceptStates

    def reset(self):
        self.currentState = self.startState

    def run(self, inputString):
        self.reset()
        occurrences = []
        text = ""
        line = 1
        for char in inputString:
            self.transition(char)
            text += char
            if char == '\n':
                line += 1
            if self.currentState is None:
                self.reset()
                text = ""
            if self.isAccepting():
                occurrences.append({
                    'text': text,
                    'linea': line,
                })
                text = ""
        return occurrences
        
    def runTables(self, inputString):
        self.reset()
        for char in inputString:
            self.transition(char)
            if self.currentState is None:
                break
        return self.isAccepting()