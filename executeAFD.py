from afd import AFD
import csv

def reportOccurrences(afd, text):
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

def main(content):
    states = {0, 1, 2, 3} 
    alphabet = {'a', 'b'} 
    transitions = {
        (1, ' '): 1, 
        (1, '\t'): 1,
        
        #Do while loop
        (1, 'd'): 2, 
        (2, 'o'): 3, 
        (3, ' '): 3,
        (3, '\t'): 3,
        (3, '{'): 4,
        
        #While loop
        (1, 'w'): 12,
        (12, 'h'): 13,
        (13, 'i'): 14,
        (14, 'l'): 15,
        (15, 'e'): 17,
        
        #For loop
        (1, 'f'): 20,
        (20, 'o'): 21,
        (21, 'r'): 22,

        } 
    startState = 0
    acceptStates = {2}
    afd = AFD(states, alphabet, transitions, startState, acceptStates)
    text = content
    occurrences = reportOccurrences(afd, text)
    return occurrences
