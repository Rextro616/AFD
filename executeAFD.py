from afd import AFD
import csv

def reportOccurrences(afd, patterns, text):
    occurrences = []
    for row_num, line in enumerate(text, start=1):
        for col_num, char in enumerate(line, start=1):
            if afd.run(char):
                occurrences.append({
                    'fila': row_num,
                    'columna': col_num,
                    'texto': char
                })
    return occurrences

def main():
    states = {0, 1, 2, 3} 
    alphabet = {'a', 'b'} 
    transitions = {(0, 'a'): 1, (1, 'b'): 2} 
    startState = 0
    acceptStates = {2}
    afd = AFD(states, alphabet, transitions, startState, acceptStates)
    patterns = 
    text = 
    occurrences = reportOccurrences(afd, patterns, text)
    return occurrences
