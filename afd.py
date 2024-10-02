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
        lines = [line]
        for char in inputString:
            self.transition(char)
            text += char
            if char == '\n':
                line += 1
                lines.append(line)
            if self.currentState is None:
                self.reset()
                text = ""
                lines = [line]
            if self.isAccepting():
                occurrences.append({
                    'text': text,
                    'lineas': f"{lines[0]} a la {line}" if len(lines) > 1 else f"{line}"
                })
                text = ""
                lines = [line]
        return occurrences
        
    def runTables(self, inputString):
        self.reset()
        for char in inputString:
            self.transition(char)
            if self.currentState is None:
                break
        return self.isAccepting()